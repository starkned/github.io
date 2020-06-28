import pygame
import sys
import main

class Deadmenu:


    def __init__(self, screen):
        self.screen = screen
        self.info()
        self.update()

    def draw(self):
        pass

    def update(self):
        pygame.display.update()

    def info(self):
        my_font = pygame.font.SysFont('宋体', 16, True)

        self.screen.blit(my_font.render(u'当前得分: %d' % Deadmenu.score, True, [255, 0, 0]), [20, 20])
