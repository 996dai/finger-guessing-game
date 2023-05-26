#!
# -*- coding:UTF-8 -*-
"""
@Author : daichangcheng
@day : 2022/1/22 0022 22:18
"""
import os.path
import random
import time
import pygame
import sys
import imgg

pygame.init()
background_x = 700
background_y = 500
screen = pygame.display.set_mode((background_x, background_y))
pygame.display.set_caption('剪刀石头布')
game_over_text2 = pygame.image.load("img/开始游戏.gif").convert_alpha()
game_over_rect = game_over_text2.get_rect()
#
# x = 0
# u = 1
# while u:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#     # 打印矩形
#     pygame.draw.rect(screen, [230, 230, 230],
#                      [0, 0, background_x - 1, background_y - 1], 0)
#     screen.blit(game_over_text2, (background_x / 2 - game_over_rect[2] / 2,
#                                   background_y / 2 - game_over_rect[3] / 2))
#
#     # 文字
#     # 导入字体
#     welcome_font = pygame.font.Font("font/font.ttf", 150)
#     welcome_text = welcome_font.render("*welcome*", True, (100, 200, 255))
#     wc_size = welcome_text.get_size()
#     x += 1
#
#     screen.blit(welcome_text, (background_x / 2 - wc_size[0] / 2, 5))
#     pygame.display.flip()
#     if x == 1500:
#         u = 0
# y = input("退吗")
# if y == 't':
#     u = 0
# while 1:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#     screen_1 = pygame.display.set_mode((background_x, background_y))
#     pygame.draw.rect(screen_1, [200, 20, 230],
#                      [0, 0, background_x - 1, background_y - 1], 0)
#     pygame.display.flip()


# print(game_over_rect.bottom)
# pos = pygame.mouse.get_pos()
# print(os.path.exists('score.txt'))
#
# robot = random.randint(0, 3)
# print(robot)
# 如果用户点击“重新开始”
#         if game_over_rect.left< pos[0] < game_over_rect.right and\
#            game_over_rect.top < pos[1] < game_over_rect.bottom:
#             # 重新开始
#             main()


# ts = int(time.time())
# print('这个第一%d' % ts)

# stop = 0
# p = 1
# t = input('kai')
# while t == 'kai':
#     if p:
#         stop = int(time.time())
#         print('这个第一%d' % stop)
#         p = 0
#     if int(time.time()) - stop == 2:
#         print('这个第二%d' % int(time.time()))
a = imgg.Images()
print(a.continue_i_rect)



print(max(4, 77))
# jv = int(input('局数：'))
# fen = int(input('分数：'))
#
#
# f = open('score.txt', 'r')
# re = f.read()
# jv_max = max(jv, int(re.split(',')[0]))
# fen_max = max(fen, int(re.split(',')[1]))
# f.close()
#
# c = open('score.txt', 'w')
# c.write(str(f'{jv_max},{fen_max}'))
# t = 0
# f.close()
