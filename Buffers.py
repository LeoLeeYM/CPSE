import win32console,win32con
import traceback, time

virtual_keys={}
for k,v in win32con.__dict__.items():
    if k.startswith('VK_'):
        virtual_keys[v]=k 

free_console=True
    ## only free console if one was created successfully

stdout=win32console.GetStdHandle(win32console.STD_OUTPUT_HANDLE)
stdin=win32console.GetStdHandle(win32console.STD_INPUT_HANDLE)
#控制台双缓冲实现
class Buffers():
    def __init__(self, num=2):
        '''
        控制台多缓冲区
        '''
        self.__num = num
        self.__buffer_list = []
        self.__create_buffers()
        self.__current = 0
        self.__last = 0

    def __create_buffers(self):
        for i in range(self.__num):
            self.__buffer_list.append(win32console.CreateConsoleScreenBuffer())

    def print(self, str_='\n',color_ = 0x07):
        '''
        向缓冲区输入内容
        '''
        self.__buffer_list[self.__current].SetConsoleTextAttribute(color_)
        self.__buffer_list[self.__current].WriteConsole(str_)

    def switch(self):
        '''
        切换刷新缓冲区
        '''
        self.__last = self.__current
        self.__current = (self.__current + 1) % self.__num
        self.__buffer_list[self.__current] = win32console.CreateConsoleScreenBuffer()

    def flash(self):
        '''
        刷新显示缓冲区
        '''
        self.__buffer_list[self.__current].SetConsoleActiveScreenBuffer()   # 使当前缓冲区可见
        self.__buffer_list[self.__last].Close() # 关闭上一个缓冲区