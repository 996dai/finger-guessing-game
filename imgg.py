#!
# -*- coding:UTF-8 -*-
"""
@Author : daichangcheng
@day : 2022/1/23 0023 11:47
"""
import pygame


class Images:
    # 录入图片
    def __init__(self):
        self.start = pygame.image.load("img/开始游戏.gif").convert_alpha()
        self.start_rect = self.start.get_rect()

        self.max = pygame.image.load("img/最高分.png").convert_alpha()
        self.max_rect = self.max.get_rect()

        self.quit = pygame.image.load("img/退出游戏.png").convert_alpha()
        self.quit_rect = self.quit.get_rect()

        self.game_continue = pygame.image.load("img/继续游戏.png").convert_alpha()
        self.game_continue_rect = self.game_continue.get_rect()

        self.pause = pygame.image.load("img/暂停.png").convert_alpha()
        self.pause_rect = self.pause.get_rect()

        self.continue_i = pygame.image.load("img/继续.png").convert_alpha()
        self.continue_i_rect = self.continue_i.get_rect()

        self.star = pygame.image.load("img/星.png").convert_alpha()
        self.star_rect = self.star.get_rect()

        self.b1 = pygame.image.load("img/1b.png").convert_alpha()
        self.b1_rect = self.b1.get_rect()

        self.j1 = pygame.image.load("img/1j.png").convert_alpha()
        self.j1_rect = self.j1.get_rect()

        self.s1 = pygame.image.load("img/1s.png").convert_alpha()
        self.s1_rect = self.s1.get_rect()

        self.b2 = pygame.image.load("img/2b.png").convert_alpha()
        self.b2_rect = self.b2.get_rect()

        self.j2 = pygame.image.load("img/2j.png").convert_alpha()
        self.j2_rect = self.j2.get_rect()

        self.s2 = pygame.image.load("img/2s.png").convert_alpha()
        self.s2_rect = self.s2.get_rect()


