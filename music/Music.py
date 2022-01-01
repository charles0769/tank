'''
音效类
author:Charles Su
create on 2021-12-26 23:18:48
'''
import pygame


class Music():
    def __init__(self,fileName) -> None:
        self.fileName = fileName
        # 加载进模块
        pygame.mixer.init()
        pygame.mixer.music.load(self.fileName)
    
    # 播放音乐
    def play(self):
        pygame.mixer.music.play()