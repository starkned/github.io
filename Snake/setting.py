import pygame
import sys
from pygame.locals import *
import mainmenu, main
import constants as C


class Setting:
    text_color = [C.redColor, C.blackColor, C.redColor, C.redColor, C.redColor]
    choice =1
    def __init__(self, screen):

        self.screen = screen
        self.create_background()
        self.create_info_label()
        self.change()

        self.update()

    def create_background(self):
        bgpic = pygame.image.load("background.jpg")
        bgpic = pygame.transform.scale(bgpic, (640, 480))
        self.screen.blit(bgpic, (0, 0))

    def create_info_label(self):
        font = pygame.font.Font(None, 48)

        text1 = font.render("speed", 1, Setting.text_color[0])
        text2 = font.render("1", 1, Setting.text_color[1])
        text3 = font.render("2", 1, Setting.text_color[2])
        text4 = font.render("3", 1, Setting.text_color[3])
        text5 = font.render("back", 1, Setting.text_color[4])
        self.screen.blit(text1, (275, 100))
        self.screen.blit(text2, (275, 150))
        self.screen.blit(text3, (275, 200))
        self.screen.blit(text4, (275, 250))
        self.screen.blit(text5, (275, 300))

    def change(self):
        for event in pygame.event.get():
            # 判断是否为退出事件
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # 按键事件
            elif event.type == KEYDOWN:
                if event.key == K_s and Setting.choice in range(1, 5):
                    Setting.choice += 1
                    Setting.text_color[Setting.choice-1]=C.redColor
                    Setting.text_color[Setting.choice] = C.blackColor
                elif event.key == K_w and Setting.choice in range(2, 5):
                    Setting.choice -= 1
                    Setting.text_color[Setting.choice +1] = C.redColor
                    Setting.text_color[Setting.choice] = C.blackColor
                elif event.key == K_RETURN:
                    if Setting.choice != 4:
                        C.SPEED = 10 * Setting.choice
                    mainmenu.mainMenu.state = "mainmenu"

    def back(self):
        for event in pygame.event.get():
            # 判断是否为退出事件
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # 按键事件
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    mainmenu.mainMenu.state = "mainmenu"

    def update(self):
        self.back()
        pygame.display.update()
