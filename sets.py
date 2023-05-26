#!
# -*- coding:UTF-8 -*-
"""
@Author : daichangcheng
@day : 2022/1/23 0023 11:30
"""
import pygame


class Sets:

    def __init__(self):
        """"设置屏幕参数"""
        self.music = None
        self.robot_size = None
        self.robot_font = None
        self.robot_text = None
        self.screen_width = 700
        self.screen_height = 500
        self.bg_color = [230, 230, 230]
        pygame.init()
        pygame.mixer.init()

        """字体参数"""
        # 主页欢迎字
        self.welcome_font = pygame.font.Font("font/font.ttf", 150)
        self.welcome_text = self.welcome_font.render("*welcome*", True, (100, 200, 255))
        self.welcome_size = self.welcome_text.get_size()  # (长，宽)

        # 作者署名
        self.dcc_font = pygame.font.Font("font/rough.ttf", 50)
        self.dcc_text = self.dcc_font.render("作者:Dcc", True, (100, 200, 255))
        self.dcc_size = self.dcc_text.get_size()  # (长，宽)

        # 最高分显示样式
        f = open('score.txt', 'r')
        score = f.read().split(',')
        jv = score[0]
        fen = score[1]
        f.close()
        self.robot_font_max = pygame.font.Font('font/zw.ttf', 80)  # 最高分文字
        self.robot_text_max = self.robot_font_max.render('最高得分:' + fen, True, (27, 191, 0))
        self.robot_size_max = self.robot_text_max.get_size()  # (长，宽)

        self.robot_font_max_jv = pygame.font.Font('font/zw.ttf', 80)  # 最多局文字
        self.robot_text_max_jv = self.robot_font_max_jv.render('最高局数:' + jv, True, (111, 111, 111))
        self.robot_size_max_jv = self.robot_text_max_jv.get_size()  # (长，宽)

        self.robot_font_max_f = pygame.font.Font('font/zw.ttf', 80)  # 提示文字
        self.robot_text_max_f = self.robot_font_max_f.render('点击屏幕返回', True, (60, 200, 155))
        self.robot_size_max_f = self.robot_text_max_f.get_size()  # (长，宽)

        """游戏运行页面"""
        # 我方文字
        self.robot_font_we = pygame.font.Font('font/zw.ttf', 60)
        self.robot_text_we = self.robot_font_we.render('我方', True, (59, 81, 255))
        self.robot_size_we = self.robot_text_we.get_size()  # (长，宽)
        # 敌方文字
        self.robot_font_enemy = pygame.font.Font('font/zw.ttf', 60)
        self.robot_text_enemy = self.robot_font_enemy.render('对方', True, (255, 40, 60))
        self.robot_size_enemy = self.robot_text_enemy.get_size()  # (长，宽)

        # win
        self.robot_font_win = pygame.font.Font('font/zw.ttf', 60)
        self.robot_text_win = self.robot_font_win.render('win', True, (27, 191, 0))
        self.robot_size_win = self.robot_text_win.get_size()  # (长，宽)

        # lost
        self.robot_font_lost = pygame.font.Font('font/zw.ttf', 60)
        self.robot_text_lost = self.robot_font_lost.render('lost', True, (255, 40, 60))
        self.robot_size_lost = self.robot_text_lost.get_size()  # (长，宽)

        # 平
        self.robot_font_ping = pygame.font.Font('font/zw.ttf', 60)
        self.robot_text_ping = self.robot_font_ping.render('平', True, (255, 150, 0))
        self.robot_size_ping = self.robot_text_ping.get_size()  # (长，宽)

        # VS画面
        self.robot_font = pygame.font.Font('font/font.ttf', 100)
        self.robot_text_V = self.robot_font.render('VS', True, (255, 150, 0))
        self.robot_size_V = self.robot_text_V.get_size()  # (长，宽)

        # ?号画面
        self.robot_font = pygame.font.Font('font/font.ttf', 170)
        self.robot_text_w = self.robot_font.render('?', True, (255, 180, 60))
        self.robot_size_w = self.robot_text_w.get_size()  # (长，宽)

        # 选择手势打印
        self.robot_font = pygame.font.Font('font/zw.ttf', 50)  # 石头
        self.robot_text_s = self.robot_font.render('石头', True, (100, 200, 255))
        self.robot_size = self.robot_text_s.get_size()  # (长，宽)
        self.robot_font = pygame.font.Font('font/zw.ttf', 50)  # 石头_绿
        self.robot_text_s_l = self.robot_font.render('石头', True, (27, 191, 0))
        self.robot_size = self.robot_text_s_l.get_size()  # (长，宽)

        self.robot_font = pygame.font.Font('font/zw.ttf', 50)  # 剪子
        self.robot_text_j = self.robot_font.render('剪刀', True, (100, 200, 255))
        self.robot_size = self.robot_text_j.get_size()
        self.robot_font = pygame.font.Font('font/zw.ttf', 50)  # 剪子_绿
        self.robot_text_j_l = self.robot_font.render('剪刀', True, (27, 191, 0))
        self.robot_size = self.robot_text_j_l.get_size()

        self.robot_font = pygame.font.Font('font/zw.ttf', 50)  # 布
        self.robot_text_b = self.robot_font.render('布', True, (100, 200, 255))
        self.robot_size = self.robot_text_b.get_size()
        self.robot_font = pygame.font.Font('font/zw.ttf', 50)  # 布_绿
        self.robot_text_b_l = self.robot_font.render('布', True, (27, 191, 0))
        self.robot_size = self.robot_text_b_l.get_size()

        # 得分
        self.robot_font = pygame.font.Font('font/zw.ttf', 30)
        self.robot_text_fen = self.robot_font.render('得分:', True, (255, 150, 0))
        self.robot_size_fen = self.robot_text_fen.get_size()  # (长，宽)

        # 局数
        self.robot_font = pygame.font.Font('font/zw.ttf', 30)
        self.robot_text_jv = self.robot_font.render('局数:', True, (255, 150, 0))
        self.robot_size_jv = self.robot_text_jv.get_size()  # (长，宽)

        # 机会
        self.robot_font = pygame.font.Font('font/zw.ttf', 30)
        self.robot_text_chance = self.robot_font.render('机会:', True, (255, 150, 0))
        self.robot_size_chance = self.robot_text_chance.get_size()  # (长，宽)

        # 开始较量
        self.robot_font = pygame.font.Font('font/zw.ttf', 50)
        self.robot_text_k = self.robot_font.render('开始较量', True, (111, 111, 111))
        self.robot_size_k = self.robot_text_k.get_size()  # (长，宽)
        # 开始较量_绿
        self.robot_font = pygame.font.Font('font/zw.ttf', 50)
        self.robot_text_k_l = self.robot_font.render('开始较量', True, (27, 191, 0))
        self.robot_size_k_l = self.robot_text_k_l.get_size()  # (长，宽)

        """音乐设置"""
        # 主页按键声音
        self.music_p1_key = pygame.mixer.Sound("music/p1_key.wav")
        self.music_p1_key.set_volume(0.8)

        # 游内按键声音
        self.music_p2_key = pygame.mixer.Sound("music/p2_key.wav")
        self.music_p2_key.set_volume(0.2)

        # win声音
        self.music_win = pygame.mixer.Sound("music/win_mis.wav")
        self.music_win.set_volume(1)

        # lost声音
        self.music_lost = pygame.mixer.Sound("music/lost_mis.wav")
        self.music_lost.set_volume(0.2)

        # 平的声音
        self.music_ping = pygame.mixer.Sound("music/平.wav")
        self.music_ping.set_volume(0.5)

        # 开始的声音
        self.music_kai = pygame.mixer.Sound("music/kai.wav")
        self.music_kai.set_volume(1)


if __name__ == '__main__':
    pass
