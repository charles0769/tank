'''
坦克类
 移动射击
author:Charles Su
create on 2021-12-26 23:03:46
'''
import pygame,random
import sys
sys.path.append('../')
import MainGame


class Tank:
    def __init__(self,left,top):
        self.images = {
            'U': pygame.image.load('坦克大战\\images\\tankU.gif'),
            'D': pygame.image.load('坦克大战\\images\\tankD.gif'),
            'L': pygame.image.load('坦克大战\\images\\tankL.gif'),
            'R': pygame.image.load('坦克大战\\images\\tankR.gif'),
        }
        self.direction = 'U'
        self.image = self.images[self.direction]
        
        # 坦克的所在区域
        self.rect = self.image.get_rect()
        # 指定坦克初始化位置
        self.rect.left = left
        self.rect.top = top
        # 新增速度属性
        self.speed = 5
        # 新增一个移动开关，初始化时是关的
        self.stop = True
    
    # 坦克的移动方法
    def move(self, width=0, height=0):
        # 判断目前坦克方向
        if self.direction == 'L':
            # 往左的话，rect的left属性要减少
            self.rect.left -= self.speed if self.rect.left >= self.speed else self.rect.left
        elif self.direction == 'R':
            # 往右的话，rect的left属性要增加
            self.rect.left += self.speed if self.rect.left + self.rect.height + self.speed <= width else 0
        elif self.direction == 'U':
            # 往上的话，rect的top属性要减少
            self.rect.top -= self.speed if self.rect.top >= self.speed else self.rect.top
        elif self.direction == 'D':
            # 往下的话，rect的top属性要增加
            self.rect.top += self.speed if self.rect.top + self.rect.height + self.speed <= height else 0
    
    # 坦克的射击方法
    def shoot(self):
        pass
    
    # 坦克展示(将坦克这个surface绘制到窗口中)
    def display(self,window):
        # 1.重新设置坦克的图片
        self.image = self.images[self.direction]
        # 2.将坦克加入到窗口中
        window.blit(self.image,self.rect)
        
class MyTank(Tank):
    def __init__(self,left,top):
        super().__init__(left,top)
        
class EnemyTank(Tank):
    def __init__(self,left,top,speed=5) -> None:
        self.images = {
            'U': pygame.image.load('坦克大战\\images\\InkedtankU.gif'),
            'D': pygame.image.load('坦克大战\\images\\InkedtankD.gif'),
            'L': pygame.image.load('坦克大战\\images\\InkedtankL.gif'),
            'R': pygame.image.load('坦克大战\\images\\InkedtankR.gif'),
        }
        self.direction = self.randDirection()
        self.image = self.images[self.direction]
        
        # 坦克的所在区域
        self.rect = self.image.get_rect()
        # 指定坦克初始化位置
        self.rect.left = left
        self.rect.top = top
        # 新增速度属性
        self.speed = speed
        # 新增一个移动开关，初始化时是关的
        self.stop = True
        
    def randDirection(self):
        num = random.randint(1,4)
        if num == 1:
            return 'U'
        elif num == 2:
            return 'L'
        elif num == 3:
            return 'R'
        elif num == 4:
            return 'D'
    def displayEnemtTank(self,window):
        super().display(window)