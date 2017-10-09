# -*- coding: utf-8 -*-
import sys

import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien

def run_game():

    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_sttings = Settings()
    screen = pygame.display.set_mode((ai_sttings.screen_wdith, ai_sttings.screen_height))

    pygame.display.set_caption("Alien vasion")

    ship = Ship(ai_sttings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 创建一个外星人
    alien = Alien(ai_sttings, screen)


    # 开始游戏的主循环
    while True:
        gf.check_events(ai_sttings, screen,ship,bullets)
        ship.update()
        gf.update_bullets(bullets)
        print(len(bullets))
        gf.update_screen(ai_sttings,screen,ship, alien,bullets)


run_game()