#工具和遊戲主控
import pygame
import random

class Game:
    def __init__(self):

        self.screen = pygame.display.get_surface()
        self.clock = pygame.time.Clock()
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                elif event.type == pygame.VIDEORESIZE:
                    width = max(800, event.w)
                    height = max(600, event.h)

                    if (width, height) != event.size:
                        self.screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
                elif event.type == pygame.KEYDOWN:
                    self.keys = pygame.key.get_pressed()
                elif event.type == pygame.KEYUP:
                    self.keys = pygame.key.get_pressed()
            self.screen.fill((0,0,0))
            pygame.display.update()
            self.clock.tick(60)
        