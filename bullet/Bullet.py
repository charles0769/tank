'''
子弹类
author:Charles Su
create on 2021-12-26 23:12:04
'''
import pygame
import sys
sys.path.append('../')
from baseitem.BaseItem import *
from explode.Explode import *

class Bullet(BaseItem):
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
        # 记录子弹是否活着
        self.live = True
    
    # 子弹的移动方法
    def move(self,width,height):
        if self.direction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
            else:
                # 修改状态值
                self.live = False
        elif self.direction == 'D':
            if self.rect.top < height - self.rect.height:
                self.rect.top += self.speed
            else:
                # 修改状态值
                self.live = False
        elif self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
            else:
                # 修改状态值
                self.live = False
        elif self.direction == 'R':
            if self.rect.left < width - self.rect.width:
                self.rect.left += self.speed
            else:
                # 修改状态值
                self.live = False
    
    # 展示子弹
    def display(self,window):
        window.blit(self.image, self.rect)
    
    # 新增我方子弹碰撞敌方坦克的方法
    def hitEnemyTank(self,EnemyTank_list,Explode_list):
        for eTank in EnemyTank_list:
            if pygame.sprite.collide_rect(eTank,self):
                # 产生一个爆炸效果
                explode = Explode(eTank)
                # 将爆炸效果加入到爆炸效果列表
                Explode_list.append(explode)
                # 改变子弹状态
                self.live = False
                # 改变坦克状态
                eTank.live = False
    
    # 新增敌方子弹碰撞我方坦克的方法
    def hitMyTank(self,tank,Explode_list):
        if pygame.sprite.collide_rect(self,tank):
            # 产生爆炸效果，并加入到爆炸效果列表里
            explode = Explode(tank)
            Explode_list.append(explode)
            # 修改子弹状态
            self.live = False
            # 修改坦克状态
            tank.live = False
    
    # 新增子弹与墙壁的碰撞方法
    def hitWalls(self,Wall_list):
        for wall in Wall_list:
            if pygame.sprite.collide_rect(wall,self):
                # 修改子弹的live属性
                self.live = False
                wall.hp -= 1
                if wall.hp <= 0:
                    wall.live = False
            