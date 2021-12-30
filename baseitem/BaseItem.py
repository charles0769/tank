'''
基础类
 主要用于继承pygame的精灵类
author:Charles Su
create on 2021-12-31 00:30:05
'''
import pygame
import sys
sys.path.append('../')

class BaseItem(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()