# -*- coding: utf-8 -*-
import sys

import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_sttings = Settings()
    screen = pygame.display.set_mode((ai_sttings.screen_width, ai_sttings.screen_height))

    pygame.display.set_caption("Alien vasion")
    # 创建一艘飞船、一个子弹编组、一个外星人编组
    ship = Ship(ai_sttings, screen)
    bullets = Group()
    aliens = Group()
    # 创建外星人群
    gf.create_fleet(ai_sttings, screen, ship,aliens)
    # 开始游戏的主循环
    while True:
        gf.check_events(ai_sttings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        print(len(bullets))
        gf.update_screen(ai_sttings, screen, ship, aliens, bullets)


run_game()