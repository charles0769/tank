'''
坦克类
 移动射击
author:Charles Su
create on 2021-12-26 23:03:46
'''
import pygame


class Tank:
    def __init__(self,left,top):
        self.images = {
            'U': pygame.image.load(''),
            'D': pygame.image.load(''),
            'L': pygame.image.load(''),
            'R': pygame.image.load(''),
        }
        self.direction = 'U'
        self.image = self.images[self.direction]
        
        # 坦克的所在区域
        self.rect = self.image.get_rect()
        # 指定坦克初始化位置
        self.rect.left = left
        self.rect.top = top
    
    # 坦克的移动方法
    def move(self):
        pass
    
    # 坦克的射击方法
    def shoot(self):
        pass
    
    # 坦克展示
    def display(self):
        pass