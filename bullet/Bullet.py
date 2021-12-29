'''
子弹类
author:Charles Su
create on 2021-12-26 23:12:04
'''
import pygame

class Bullet:
    def __init__(self,tank) -> None:
        # 图片
        self.images = {
            'U': pygame.image.load('坦克大战\\images\\MissileU.gif'),
            'D': pygame.image.load('坦克大战\\images\\MissileD.gif'),
            'L': pygame.image.load('坦克大战\\images\\MissileL.gif'),
            'R': pygame.image.load('坦克大战\\images\\MissileR.gif'),
        }
        # 方向(坦克方向)
        self.direction = tank.direction
        self.image = self.images[self.direction]
        # 位置
        self.rect = self.image.get_rect()
        if self.direction == 'U':
            self.rect.left = tank.rect.left + tank.rect.width/2 - self.rect.width/2
            self.rect.top = tank.rect.top - self.rect.height
        elif self.direction == 'D':
            self.rect.left = tank.rect.left + tank.rect.width/2 - self.rect.width/2
            self.rect.top = tank.rect.top + tank.rect.height + self.rect.height
        elif self.direction == 'L':
            self.rect.left = tank.rect.left - self.rect.width
            self.rect.top = tank.rect.top + tank.rect.width/2 - self.rect.width/2
        elif self.direction == 'R':
            self.rect.left = tank.rect.left + tank.rect.height + self.rect.width
            self.rect.top = tank.rect.top + tank.rect.width/2 - self.rect.width/2
        # 速度
        self.speed = 7
    
    # 子弹的移动方法
    def move(self,width,height):
        if self.direction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
            else:
                pass
        elif self.direction == 'D':
            if self.rect.top < height - self.rect.height:
                self.rect.top += self.speed
            else:
                pass
        elif self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
            else:
                pass
        elif self.direction == 'R':
            if self.rect.left < width - self.rect.width:
                self.rect.left += self.speed
            else:
                pass
    
    # 展示子弹
    def display(self,window):
        window.blit(self.image, self.rect)