'''
主逻辑类
 开始游戏
 结束游戏
author:Charles Su
create on 2021-12-26 23:00:59
'''
import pygame
from tank.Tank import *
# 将pygame.display重命名一下，方便使用
_dispaly = pygame.display
# 版本号
_VERSION = '1.0.0'

class MainGame():
    # 游戏主窗口
    window = None
    # 窗口宽度
    SCREEN_WIDTH = 800
    # 窗口高度
    SCREEN_HEIGHT = 500
    # 窗口颜色
    SCREEN_COLOR = pygame.Color(0,0,0)
    # 字体颜色
    FONT_COLOR = pygame.Color(255,0,0)
    # 我方坦克
    TANK_P1 = None
    
    def __init__(self):
        pass
    
    # 开始游戏
    def startGame(self):
        # 创建窗口，加载窗口
        _dispaly.init()
        MainGame.window = _dispaly.set_mode([MainGame.SCREEN_WIDTH,MainGame.SCREEN_HEIGHT])
        MainGame.TANK_P1 = MyTank(MainGame.SCREEN_WIDTH/2,MainGame.SCREEN_HEIGHT/2)
        # 设置标题
        _dispaly.set_caption("坦克大战{0}".format(_VERSION))
        # 让窗口持续刷新
        while True:
            # 给窗口填充一个颜色
            MainGame.window.fill(MainGame.SCREEN_COLOR)
            # 获取事件
            self.getEvent()
            # 将绘制的小画布贴到窗口里
            MainGame.window.blit(self.getTextSurface("剩余敌方坦克%d辆"%5),(5,5))
            # 将我方坦克加入到窗口
            MainGame.TANK_P1.display(MainGame.window)
            # 刷新
            _dispaly.update()
    
    # 获取程序期间所有的事件(鼠标事件，键盘事件，...)
    def getEvent(self):
        # 1.获取所有事件
        eventList = pygame.event.get()
        # 2.对事件进行判断处理(1.点击关闭按钮  2.按下键盘上的某个按键)
        for event in eventList:
            # 判断事件类型是否是退出
            if event.type == pygame.QUIT:
                self.endGame()
            # 判断事件类型是否是按键类型，如果是，判断是哪一个按键
            if event.type == pygame.KEYDOWN:
                # 判断具体是哪一个按键
                if event.key == pygame.K_LEFT:
                    # 左方向键
                    print("坦克向左调头,移动")
                elif event.key == pygame.K_RIGHT:
                    # 右方向键
                    print("坦克向右调头,移动")
                elif event.key == pygame.K_UP:
                    # 上方向键
                    print("坦克向上调头,移动")
                elif event.key == pygame.K_DOWN:
                    # 下方向键
                    print("坦克向下调头,移动")
                elif event.key == pygame.K_SPACE:
                    # 空格
                    print("坦克发射子弹")
            
    # 左上角文字绘制
    def getTextSurface(self, text):
        # 初始化字体模块
        pygame.font.init()
        # 选择一种字体
        font = pygame.font.SysFont('kaiti',18)
        # 使用对应的字符完成相关内容的绘制
        textSurface = font.render(text,True,MainGame.FONT_COLOR)
        return textSurface
    
    # 结束游戏
    def endGame(self):
        print("谢谢游玩!")
        # 结束python解释器
        exit()
    
if __name__ == '__main__':
    MainGame().startGame()