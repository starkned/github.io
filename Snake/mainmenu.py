import pygame
import sys
from pygame.locals import *
import setting
import constants as C


class mainMenu:
    state = 'mainmenu'
    cursor = 'play'
    text1_color = C.blackColor
    text2_color = C.redColor

    def __init__(self, screen):
        self.screen = screen
        self.create_background()
        self.create_info_label()
        self.enter()

        self.update()

    def create_background(self):
        bgpic = pygame.image.load("background.jpg")
        bgpic = pygame.transform.scale(bgpic, (640, 480))
        self.screen.blit(bgpic, (0, 0))

    def create_info_label(self):
        font = pygame.font.Font(None, 48)

        text1 = font.render("Play", 1, mainMenu.text1_color)
        text2 = font.render("Setting", 1, mainMenu.text2_color)
        self.screen.blit(text1, (275, 240))
        self.screen.blit(text2, (275, 280))

    def enter(self):
        for event in pygame.event.get():
            # 判断是否为退出事件
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # 按键事件
            elif event.type == KEYDOWN:
                if event.key == K_w:
                    mainMenu.cursor = 'play'
                    mainMenu.text2_color = C.redColor
                    mainMenu.text1_color = C.blackColor

                elif event.key == K_s:
                    mainMenu.cursor = 'setting'
                    mainMenu.text1_color = C.redColor
                    mainMenu.text2_color = C.blackColor

                elif event.key == K_RETURN:
                    mainMenu.state = mainMenu.cursor

                elif event.key == K_ESCAPE:
                    pygame.quit()

    def setting(self):
        mainMenu.state = 'setting'

    def update(self):
        pygame.display.update()
