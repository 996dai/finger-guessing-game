#!
# -*- coding:UTF-8 -*-
"""
@Author : daichangcheng
@day : 2022/1/25 0025 21:21
"""
import random


def run_hand(you, my):
    if you_hand == you:
        if my_hand == my:
            print("win")
        else:
            print('lost')
        print('--------')


u = 1
while u:
    hand = ['s', 'j', 'b']
    you_hand = random.choice(hand)
    print(you_hand)
    my_hand = input("s,j,b")
    if my_hand != 't':
        if my_hand == you_hand:
            print('平手')
            print('------------------')
        else:
            run_hand('s', 'b')
            run_hand('j', 's')
            run_hand('b', 'j')
    else:
        u = 0

# # 敌方随机出拳
# robot = random.randint(0, 2)
# if robot == 0:
#     self.p2_b2 = True
#     self.p2_j2 = False
#     self.p2_s2 = False
# elif robot == 1:
#     self.p2_b2 = False
#     self.p2_j2 = True
#     self.p2_s2 = False
# elif robot == 2:
#     self.p2_b2 = False
#     self.p2_j2 = False
#     self.p2_s2 = True  # 人机随机出
# p1 = False
# btn = False
# print(robot)
#
# # 人机手势
# if self.p2_b2:
#     self.screen.blit(self.images.b2,
#                      (self.sets.screen_width / 2 - self.images.b2_rect[2] / 2 + 200,
#                       self.sets.screen_height / 2 - 200))
#
# elif self.p2_j2:
#     self.screen.blit(self.images.j2,
#                      (self.sets.screen_width / 2 - self.images.b2_rect[2] / 2 + 200,
#                       self.sets.screen_height / 2 - 200))
#
# elif self.p2_s2:
#     self.screen.blit(self.images.s2,
#                      (self.sets.screen_width / 2 - self.images.b2_rect[2] / 2 + 200,
#                       self.sets.screen_height / 2 - 200))