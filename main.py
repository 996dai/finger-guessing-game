#!
# -*- coding:UTF-8 -*-
"""
@Author : daichangcheng
@day : 2022/1/22 0022 22:28
"""
import pygame
import sys
import random
import time
from imgg import Images
from sets import Sets


class Main:
    def __init__(self):
        """初始化并导入参数"""
        self.fen = 0  # 得分
        self.star_number = 3  # 星星
        self.ping = False  # 游戏平手
        self.lost = False  # 对方胜
        self.win = False  # 我方胜
        self.sleep = False  # 游戏间隔
        self.p2_b2 = False
        self.p2_j2 = False
        self.p2_s2 = False
        self.my_hand = False
        self.enemy_hand = False
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("music/无双的王者.mp3")  # 背景音乐
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(30)
        self.robot_font_jv = pygame.font.Font('font/zw.ttf', 30)  # 局数字体
        self.robot_font_fen = pygame.font.Font('font/zw.ttf', 30)  # 得分字体
        self.robot_text_jv = 0  # 局数为0
        self.robot_text_fen = 0  # 得分为0
        self.sets = Sets()  # 参数模块
        self.screen = pygame.display.set_mode(
            (self.sets.screen_width, self.sets.screen_height))
        pygame.display.set_caption('剪刀石头布')
        self.images = Images()  # 图片模块
        self.clock = pygame.time.Clock()

    #  判断输赢
    def run_hand(self, enemy, my):
        if self.enemy_hand == enemy:
            if self.my_hand == my:
                self.win = True
                self.ping = False
                self.lost = False
                self.sets.music_win.play()
                self.fen += 1
            else:
                self.ping = False
                self.win = False
                self.lost = True
                self.sets.music_lost.play()
                self.star_number -= 1

    def run_game1(self):
        """开始游戏循环"""
        continue_1 = 1  # 暂停为0 继续为1
        btn2 = 1  # 暂停界面按钮
        btn3 = 0   # 继续界面按钮
        jv = 0  # 局数
        stop = 0  # 启动游戏间隔
        zan = 1  # 间隔开始
        p1_kai = True  # 主页菜单_开始
        p1_zui = True  # 主页菜单_最高分
        p1_tui = True  # 主页菜单_退出
        btn = True  # 按键响应
        btn1 = True  # 手势按键响应
        max_btn = False  # 最高分页面
        title = False  # 开始游戏画面
        p2_b2 = False   # 对手布
        p2_j2 = False   # 对手剪刀
        p2_s2 = False   # 对手石头
        c_s = False  # 点击石头
        c_j = False  # 点击剪刀
        c_b = False  # 点击布
        c_v = True  # 问号

        while 1:
            #  按钮开关 p


            p = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        p = 1

            pos = pygame.mouse.get_pos()  # 获取鼠标位置
            # 打印矩形当背景
            pygame.draw.rect(self.screen, self.sets.bg_color,
                             [0, 0, self.sets.screen_width, self.sets.screen_height], 0)

            """游戏运行内容"""
            if title:
                # 固定的文字
                if continue_1:
                    self.screen.blit(self.sets.robot_text_we, (100, 50))  # 我方文字
                    self.screen.blit(self.sets.robot_text_enemy, (500, 50))  # 对方文字
                    self.screen.blit(self.sets.robot_text_V,
                                     (self.sets.screen_width / 2 - 40, self.sets.screen_height / 2 - 30))  # VS文字
                    self.screen.blit(self.images.continue_i, (250, 0))  # 暂停
                    self.screen.blit(self.sets.robot_text_k, (270, 420))  # 开始较量

                    self.screen.blit(self.sets.robot_text_chance, (20, 420))  # 机会
                    if self.images.star != 0:
                        for i in range(self.star_number):
                            self.screen.blit(self.images.star, (90 + i*30, 425))  # 星星

                    self.screen.blit(self.sets.robot_text_jv, (530, 420))  # 局数
                    self.robot_text_jv = self.robot_font_jv.render(str(jv), True, (111, 111, 111))  # 局数值
                    self.screen.blit(self.robot_text_jv, (600, 420))  # 局数值打印

                    self.screen.blit(self.sets.robot_text_fen, (530, 450))  # 得分
                    self.robot_text_fen = self.robot_font_fen.render(str(self.fen), True, (27, 191, 0))  # 得分值
                    self.screen.blit(self.robot_text_fen, (600, 455))  # 得分值打印

                    if c_v:
                        self.screen.blit(self.sets.robot_text_w, (520, 140))  # 问号

                    #  对方随机出拳
                    if p2_b2:
                        self.screen.blit(self.images.b2,
                                         (self.sets.screen_width / 2 - self.images.b2_rect[2] / 2 + 200,
                                          self.sets.screen_height / 2 - 120))
                    if p2_j2:
                        self.screen.blit(self.images.j2,
                                         (self.sets.screen_width / 2 - self.images.b2_rect[2] / 2 + 200,
                                          self.sets.screen_height / 2 - 100))
                    if p2_s2:
                        self.screen.blit(self.images.s2,
                                         (self.sets.screen_width / 2 - self.images.b2_rect[2] / 2 + 250,
                                          self.sets.screen_height / 2 - 150))

                    # 选择手势文字
                    self.screen.blit(self.sets.robot_text_s,
                                     (self.sets.screen_width / 2 - 250,
                                      self.sets.screen_height / 2 + 100))
                    if c_s:
                        self.screen.blit(self.sets.robot_text_s_l,
                                         (self.sets.screen_width / 2 - 250,
                                          self.sets.screen_height / 2 + 100))  # 点击石头
                        self.screen.blit(self.images.s1, (80, 130))
                    # ----------------------------------------------------------------------------------------
                    self.screen.blit(self.sets.robot_text_j,
                                     (self.sets.screen_width / 2 - 35,
                                      self.sets.screen_height / 2 + 100))
                    if c_j:
                        self.screen.blit(self.sets.robot_text_j_l,
                                         (self.sets.screen_width / 2 - 35,
                                          self.sets.screen_height / 2 + 100))  # 点击剪刀
                        self.screen.blit(self.images.j1, (60, 160))
                    # ----------------------------------------------------------------------------------------
                    self.screen.blit(self.sets.robot_text_b,
                                     (self.sets.screen_width / 2 + 180,
                                      self.sets.screen_height / 2 + 100))
                    if c_b:
                        self.screen.blit(self.sets.robot_text_b_l,
                                         (self.sets.screen_width / 2 + 180,
                                          self.sets.screen_height / 2 + 100))  # 点击布
                        self.screen.blit(self.images.b1, (40, 100))

                    if self.ping:
                        self.screen.blit(self.sets.robot_text_ping,
                                         (self.sets.screen_width / 2 - 20, self.sets.screen_height / 2 - 90))
                    if self.win:
                        self.screen.blit(self.sets.robot_text_win,
                                         (self.sets.screen_width / 2 - 35, self.sets.screen_height / 2 - 90))
                    if self.lost:
                        self.screen.blit(self.sets.robot_text_lost,
                                         (self.sets.screen_width / 2 - 35, self.sets.screen_height / 2 - 90))

                    # 暂停两秒
                    if self.sleep:
                        if zan:
                            stop = int(time.time())
                            zan = 0
                            btn1 = 0
                            jv += 1
                            self.robot_text_jv = self.robot_font_jv.render(str(jv), True, (255, 150, 0))  # 局数值
                        if int(time.time()) - stop == 2:
                            p2_b2 = False
                            p2_j2 = False
                            p2_s2 = False
                            c_s = False
                            c_j = False
                            c_b = False
                            c_v = True
                            self.win = False
                            self.ping = False
                            self.lost = False
                            self.sleep = False
                            btn1 = 1
                            # 生命为0结束：
                            if self.star_number == 0:
                                title = 0
                                p1_kai = True
                                p1_zui = True
                                p1_tui = True
                                btn = True
                                p = 0

                                # 打开文件读取 分数，局数
                                f = open('score.txt', 'r')
                                re = f.read()
                                jv_max = max(jv, int(re.split(',')[0]))
                                fen_max = max(self.fen, int(re.split(',')[1]))
                                f.close()
                                # 打开文件写入 分数，局数
                                c = open('score.txt', 'w')
                                c.write(f'{jv_max},{fen_max}')
                                c.close()
                                self.sets = Sets()  # 参数模块
                                self.fen = 0  # 得分
                                jv = 0  # 局数
                                self.star_number = 3

                    # 局内按键响应
                    if self.sets.screen_width / 2 - 250 < pos[0] < self.sets.screen_width / 2 - 200 + self.sets.robot_size[
                        0] and \
                            self.sets.screen_height / 2 + 100 < pos[1] < self.sets.screen_height / 2 + 100 + \
                            self.sets.robot_size[1] and p and btn1:
                        c_s = True
                        c_j = False
                        c_b = False
                        self.my_hand = 's'
                        self.sets.music_p2_key.play()
                    if self.sets.screen_width / 2 - 45 < pos[0] < self.sets.screen_width / 2 - 5 + self.sets.robot_size[
                        0] and \
                            self.sets.screen_height / 2 + 100 < pos[1] < self.sets.screen_height / 2 + 100 + \
                            self.sets.robot_size[1] and p and btn1:
                        c_s = False
                        c_j = True
                        c_b = False
                        self.my_hand = 'j'
                        self.sets.music_p2_key.play()
                    if self.sets.screen_width / 2 + 180 < pos[0] < self.sets.screen_width / 2 + 180 + self.sets.robot_size[
                        0] and \
                            self.sets.screen_height / 2 + 100 < pos[1] < self.sets.screen_height / 2 + 100 + \
                            self.sets.robot_size[1] and p and btn1:
                        c_s = False
                        c_j = False
                        c_b = True
                        self.my_hand = 'b'
                        self.sets.music_p2_key.play()

                    if c_b or c_s or c_j:
                        self.screen.blit(self.sets.robot_text_k_l, (270, 420))  # 开始较量_绿
                        if 250 < pos[0] < 250 + self.sets.robot_size_k_l[0] and \
                                420 < pos[1] < 420 + self.sets.robot_size_k_l[1] and p and btn1:
                            c_v = False
                            self.sets.music_kai.play()
                            robot = random.randint(0, 2)
                            if robot == 0:
                                p2_b2 = True
                                p2_j2 = False
                                p2_s2 = False
                                self.enemy_hand = 'b'
                            elif robot == 1:
                                p2_b2 = False
                                p2_j2 = True
                                p2_s2 = False
                                self.enemy_hand = 'j'
                            elif robot == 2:
                                p2_b2 = False
                                p2_j2 = False
                                p2_s2 = True
                                self.enemy_hand = 's'  # 人机随机出

                            # win,lost,平,
                            if self.my_hand == self.enemy_hand:
                                self.ping = True
                                self.win = False
                                self.lost = False
                                self.sets.music_ping.play()
                                if self.star_number < 3:
                                    self.star_number += 1
                            else:
                                self.run_hand('s', 'b')
                                self.run_hand('j', 's')
                                self.run_hand('b', 'j')

                            self.sleep = True
                            zan = 1
                            self.my_hand = False
                            self.enemy_hand = False
                # 点击暂停
                if 250 < pos[0] < 450 and 0 < pos[1] < 155 and p and btn2:
                    continue_1 = 0
                    p = 0
                    btn2 = 0
                    btn3 = 1

                # 暂停画面
                if continue_1 == 0:
                    self.screen.blit(self.images.pause, (300, 0))
                    if 300 < pos[0] < 420 and 0 < pos[1] < 146 and p and btn3:
                        continue_1 = 1
                        btn2 = 1
                        btn3 = 0

            """主页画面"""
            # 开始的图片
            if p1_kai:
                self.screen.blit(self.images.start,
                                 (self.sets.screen_width / 2 - self.images.start_rect[2] / 2,
                                  self.sets.screen_height / 2 - 100))
                self.images.start_rect.left = self.sets.screen_width / 2 - self.images.start_rect[2] / 2
                self.images.start_rect.right = self.sets.screen_width / 2 + self.images.start_rect[2] / 2
                self.images.start_rect.top = self.sets.screen_height / 2 - 100
                self.images.start_rect.bottom = self.sets.screen_height / 2 - 100 + self.images.start_rect[3]

            # 最高分图片
            if p1_zui:
                self.screen.blit(self.images.max,
                                 (self.sets.screen_width / 2 - self.images.max_rect[2] / 2,
                                  self.sets.screen_height / 2 + 15))
                self.images.max_rect.left = self.sets.screen_width / 2 - self.images.max_rect[2] / 2
                self.images.max_rect.right = self.sets.screen_width / 2 + self.images.max_rect[2] / 2
                self.images.max_rect.top = self.sets.screen_height / 2 + 15
                self.images.max_rect.bottom = self.sets.screen_height / 2 + 15 + self.images.max_rect[3]

            # 退出图片
            if p1_tui:
                self.screen.blit(self.images.quit,
                                 (self.sets.screen_width / 2 - self.images.quit_rect[2] / 2,
                                  self.sets.screen_height / 2 + 120))
                self.images.quit_rect.left = self.sets.screen_width / 2 - self.images.quit_rect[2] / 2
                self.images.quit_rect.right = self.sets.screen_width / 2 + self.images.quit_rect[2] / 2
                self.images.quit_rect.top = self.sets.screen_height / 2 + 120
                self.images.quit_rect.bottom = self.sets.screen_height / 2 + 120 + self.images.quit_rect[3]

            # 标题的文字
            if p1_kai:
                self.screen.blit(self.sets.welcome_text,
                                 (self.sets.screen_width / 2 - self.sets.welcome_size[0] / 2, 5))
                self.screen.blit(self.sets.dcc_text,
                                 (self.sets.screen_width / 2 - self.sets.dcc_size[0] / 2 + 200, 400))

            # 最高分显示
            if max_btn:
                self.screen.blit(self.sets.robot_text_max,
                                 (self.sets.screen_width / 2 - 200,
                                  self.sets.screen_height / 2 - 100))

                self.screen.blit(self.sets.robot_text_max_jv,
                                 (self.sets.screen_width / 2 - 200,
                                  self.sets.screen_height / 2 - 200))

                self.screen.blit(self.sets.robot_text_max_f,
                                 (self.sets.screen_width / 2 - 230,
                                  self.sets.screen_height / 2))
                # 　 返回
                if 0 < pos[0] < self.sets.screen_width and p and max_btn:
                    p = 0
                    p1_kai = True  # 主页菜单_开始
                    p1_zui = True  # 主页菜单_最高分
                    p1_tui = True  # 主页菜单_退出
                    btn = True
                    max_btn = False

            pygame.display.update()
            self.clock.tick(30)

            """按钮功能"""
            # 开始按钮
            if self.images.start_rect.left < pos[0] < self.images.start_rect.right and \
                    self.images.start_rect.top < pos[1] < self.images.start_rect.bottom and p and btn and p1_kai:
                p1_kai = False
                p1_zui = False
                p1_tui = False
                btn = 0
                title = True
                self.sets.music_p1_key.play()

            # 最高分按钮
            elif self.images.max_rect.left < pos[0] < self.images.max_rect.right and \
                    self.images.max_rect.top < pos[1] < self.images.max_rect.bottom and p and btn and p1_zui:
                p1_kai = False
                p1_zui = False
                p1_tui = False
                btn = 0
                max_btn = True
                self.sets.music_p1_key.play()

            # 退出按钮
            elif self.images.quit_rect.left < pos[0] < self.images.quit_rect.right and \
                    self.images.quit_rect.top < pos[1] < self.images.quit_rect.bottom and p and btn and p1_tui:
                self.sets.music_p1_key.play()
                sys.exit()


if __name__ == '__main__':
    # 运行
    my_game = Main()
    my_game.run_game1()
