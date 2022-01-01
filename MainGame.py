'''
主逻辑类
 开始游戏
 结束游戏
author:Charles Su
create on 2021-12-26 23:00:59
'''
import pygame,time
from tank.Tank import *
from bullet.Bullet import *
from wall.Wall import *
from music.Music import *
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
    # 敌方坦克
    EnemyTank_list = []
    # 敌方坦克数量
    EnemyTank_count = 5
    # 存储我方坦克子弹的列表
    Bullet_list = []
    # 存储敌方坦克子弹的列表
    eBullet_list = []
    # 存储爆炸效果列表
    Explode_list = []
    # 存储墙壁的列表
    Wall_list = []
    
    def __init__(self):
        pass
    
    # 开始游戏
    def startGame(self):
        # 创建窗口，加载窗口
        _dispaly.init()
        MainGame.window = _dispaly.set_mode([MainGame.SCREEN_WIDTH,MainGame.SCREEN_HEIGHT])
        # 创建我方坦克
        self.createMyTank()
        # 创建敌方坦克
        self.createEnemyTank()
        # 创建墙壁
        self.createWalls()
        # 设置标题
        _dispaly.set_caption("坦克大战{0}".format(_VERSION))
        # 让窗口持续刷新
        while True:
            # 给窗口填充一个颜色
            MainGame.window.fill(MainGame.SCREEN_COLOR)
            # 调用展示墙壁的效果
            self.blitWalls()
            # 获取事件
            self.getEvent()
            # 将绘制的小画布贴到窗口里
            MainGame.window.blit(self.getTextSurface("剩余敌方坦克%d辆"%len(MainGame.EnemyTank_list)),(5,5))
            # 将我方坦克加入到窗口
            if MainGame.TANK_P1 and MainGame.TANK_P1.live:
                MainGame.TANK_P1.display(MainGame.window)
            else:
                del MainGame.TANK_P1
                MainGame.TANK_P1 = None
            # 将敌方坦克加入到窗口
            self.blitEnemyTank()
            # 根据坦克的移动开关状态，调用坦克的移动方法
            if MainGame.TANK_P1 and not MainGame.TANK_P1.stop:
                MainGame.TANK_P1.move(MainGame.SCREEN_WIDTH,MainGame.SCREEN_HEIGHT)
                # 移动后，调用判断是否碰撞墙壁的方法
                MainGame.TANK_P1.hitWalls(MainGame.Wall_list)
                # 移动后，调用判断是否碰撞敌方坦克的方法
                MainGame.TANK_P1.hitEnemyTank(MainGame.EnemyTank_list)
            # 渲染我方子弹
            self.blitBullet()
            # 渲染敌方子弹
            self.blitEnemyBullet()
            # 调用展示爆炸效果的方法
            self.displayExplodes()
            # 降低画布刷新率
            time.sleep(0.02)
            # 刷新
            _dispaly.update()
    
    # 创建我方坦克
    def createMyTank(self):
        MainGame.TANK_P1 = MyTank(MainGame.SCREEN_WIDTH/2,MainGame.SCREEN_HEIGHT/2)
    
    # 创建敌方坦克
    def createEnemyTank(self):
        top = 100
        for i in range(MainGame.EnemyTank_count):
            # 随机生成一个速度
            speed = random.randint(3,7)
            # 每次都随机生成一个left值
            left = random.randint(1, MainGame.SCREEN_WIDTH/100 - 1) * 100
            eTank = EnemyTank(left,top,speed)
            MainGame.EnemyTank_list.append(eTank)
    
    # 创建墙壁
    def createWalls(self):
        # 随机生成5块qiangbi 
        for i in range(6):
            wall = Wall(110*i,MainGame.SCREEN_HEIGHT/3)
            MainGame.Wall_list.append(wall)
    
    # 将墙壁加入到窗口
    def blitWalls(self):
        for  wall in MainGame.Wall_list:
            if wall.live:
                wall.display(MainGame.window)
            else:
                MainGame.Wall_list.remove(wall)
    
    # 将敌方坦克加入到窗口中
    def blitEnemyTank(self):
        for eTank in MainGame.EnemyTank_list:
            if eTank.live:
                eTank.displayEnemtTank(MainGame.window)
                # 敌方坦克移动
                eTank.randMove(MainGame.SCREEN_WIDTH,MainGame.SCREEN_HEIGHT)
                # 移动后，调用判断是否碰撞墙壁的方法
                eTank.hitWalls(MainGame.Wall_list)
                # 移动后，调用判断是否碰撞我方坦克的方法
                if MainGame.TANK_P1:
                    eTank.hitMyTank(MainGame.TANK_P1)
                if len(MainGame.EnemyTank_list) > 0:
                    eTank.hitEnemyTank(MainGame.EnemyTank_list)
                # 敌方坦克射击
                eBullet = eTank.shoot()
                # 如果子弹为None，不加入列表
                if eBullet:
                      MainGame.eBullet_list.append(eBullet)
            else:
                MainGame.EnemyTank_list.remove(eTank)
    
    # 将我方子弹加入到窗口中
    def blitBullet(self):
        for bullets in MainGame.Bullet_list:
            # 如果子弹还活着，就渲染，否则从列表中移除
            if bullets.live:
                bullets.display(MainGame.window)
                # 让子弹移动
                bullets.move(MainGame.SCREEN_WIDTH,MainGame.SCREEN_HEIGHT)
                # 调用我方子弹碰撞敌方坦克的方法
                bullets.hitEnemyTank(MainGame.EnemyTank_list,MainGame.Explode_list)
                # 调用子弹撞击墙壁的方法
                bullets.hitWalls(MainGame.Wall_list)
            else:
                MainGame.Bullet_list.remove(bullets)
    
    # 将敌方子弹加入到窗口中
    def blitEnemyBullet(self):
        for eBullet in MainGame.eBullet_list:
            # 如果子弹还活着，就渲染，否则从列表中移除
            if eBullet.live:
                eBullet.display(MainGame.window)
                # 让子弹移动
                eBullet.move(MainGame.SCREEN_WIDTH,MainGame.SCREEN_HEIGHT)
                # 调用敌方子弹碰撞我方坦克的方法
                if MainGame.TANK_P1 and MainGame.TANK_P1.live:
                    eBullet.hitMyTank(MainGame.TANK_P1,MainGame.Explode_list)
                # 调用子弹撞击墙壁的方法
                eBullet.hitWalls(MainGame.Wall_list)
            else:
                MainGame.eBullet_list.remove(eBullet)
    
    # 新增方法，展示爆炸效果
    def displayExplodes(self):
        for explode in MainGame.Explode_list:
            if explode.live:
                explode.display(MainGame.window)
            else:
                MainGame.Explode_list.remove(explode)
    
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
                # 点击ESC键，让我方坦克重生
                if event.key == pygame.K_ESCAPE and not MainGame.TANK_P1:
                    print("我方坦克重生")
                    # 调用创建我方坦克的方法
                    self.createMyTank()
                if MainGame.TANK_P1 and MainGame.TANK_P1.live:
                    # 判断具体是哪一个按键
                    if event.key == pygame.K_LEFT:
                        # 左方向键
                        print("坦克向左调头,移动")
                        # 修改坦克方向
                        MainGame.TANK_P1.direction = 'L'
                        # 根据速度移动坦克---优化放到循环里去了
                        # MainGame.TANK_P1.move()
                        # 优化为点击按键，改变坦克移动状态
                        MainGame.TANK_P1.stop = False
                    elif event.key == pygame.K_RIGHT:
                        # 右方向键
                        print("坦克向右调头,移动")
                        # 修改坦克方向
                        MainGame.TANK_P1.direction = 'R'
                        # 根据速度移动坦克---优化放到循环里去了
                        # MainGame.TANK_P1.move(MainGame.SCREEN_WIDTH)
                        # 优化为点击按键，改变坦克移动状态
                        MainGame.TANK_P1.stop = False
                    elif event.key == pygame.K_UP:
                        # 上方向键
                        print("坦克向上调头,移动")
                        # 修改坦克方向
                        MainGame.TANK_P1.direction = 'U'
                        # 根据速度移动坦克---优化放到循环里去了
                        # MainGame.TANK_P1.move()
                        # 优化为点击按键，改变坦克移动状态
                        MainGame.TANK_P1.stop = False
                    elif event.key == pygame.K_DOWN:
                        # 下方向键
                        print("坦克向下调头,移动")
                        # 修改坦克方向
                        MainGame.TANK_P1.direction = 'D'
                        # 根据速度移动坦克---优化放到循环里去了
                        # MainGame.TANK_P1.move(MainGame.SCREEN_HEIGHT)
                        # 优化为点击按键，改变坦克移动状态
                        MainGame.TANK_P1.stop = False
                    elif event.key == pygame.K_SPACE:
                        # 空格
                        if len(MainGame.Bullet_list) < 5:
                            # 产生一颗子弹
                            m = Bullet(MainGame.TANK_P1)
                            # 将子弹加入到子弹列表
                            MainGame.Bullet_list.append(m)
                            print("坦克发射子弹,当前子弹数量为:%d"%(len(MainGame.Bullet_list)))
                            # 初始化音效
                            music = Music('坦克大战\\music\\music\\fire.wav')
                            music.play()
                        else:
                            print("子弹数量不足,当前子弹数量为:%d"%(len(MainGame.Bullet_list)))
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    if MainGame.TANK_P1 and MainGame.TANK_P1.live:
                        # 当方向键按键松开时，将坦克的状态改成停止
                        MainGame.TANK_P1.stop = True
            
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