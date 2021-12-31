'''
爆炸效果类
author:Charles Su
create on 2021-12-26 23:15:21
'''
import pygame

class Explode:
    def __init__(self,tank) -> None:
        # 爆炸效果的位置就是敌方坦克的问题
        self.rect = tank.rect
        # 目前的爆炸层级
        self.step = 0
        # 各个层级的图片集合
        self.images = [
            pygame.image.load('坦克大战\\images\\0.gif'),
            pygame.image.load('坦克大战\\images\\1.gif'),
            pygame.image.load('坦克大战\\images\\2.gif'),
            pygame.image.load('坦克大战\\images\\3.gif'),
            pygame.image.load('坦克大战\\images\\4.gif'),
            pygame.image.load('坦克大战\\images\\5.gif'),
            pygame.image.load('坦克大战\\images\\6.gif'),
            pygame.image.load('坦克大战\\images\\7.gif'),
            pygame.image.load('坦克大战\\images\\8.gif'),
            pygame.image.load('坦克大战\\images\\9.gif'),
            pygame.image.load('坦克大战\\images\\10.gif'),
        ]
        # 目前层级的图片
        self.image = self.images[self.step]
        # 爆炸效果的状态，控制它的消失
        self.live = True
        
    
    # 展示爆炸效果
    def display(self,window):
        if self.step < len(self.images):
            window.blit(self.image,self.rect)
            self.image = self.images[self.step]
            self.step += 1
        else:
            # 爆炸消失，改变状态
            self.live = False
            # 将层级改回初始层级
            self.step = 0