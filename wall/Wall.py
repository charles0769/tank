'''
墙壁类
author:Charles Su
create on 2021-12-26 23:17:03
'''
import pygame

class Wall():
    def __init__(self,left,top) -> None:
        self.image = pygame.image.load('坦克大战\\images\\2.png')
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top
        # 用来判断墙壁是否应该在窗口中展示
        self.live = True
        # 用来记录墙壁的生命值
        self.hp = 3
    
    # 展示墙壁的方法
    def display(self,window):
        window.blit(self.image,self.rect)