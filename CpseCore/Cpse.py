from Buffers import *
import time
import CpseObject
import CpseFrame
import CpsePhysics
import threading
from pynput import keyboard
import copy

cpseRenderingFont = ["■","▲","△","●","◆","◇","○","▼","▽"]

buffer = Buffers()
bufferPrint = buffer.print

#region 调用函数及类
def CpseRendering(ce,frame,maxFPs,updata):

    while ce.showCRO[0]:
        updata()
        ce.ShowCRObj(ce.RenderingFrame(frame))
        
        time.sleep(1/maxFPs)

def Run(_time,fun):
    global time
    time.sleep(_time)
    fun()

def RunRe(_time,fun):
    global time
    while True:
        time.sleep(_time)
        fun()

#region 按键监视
keyboardOnclick = []
key = keyboard.Key
def KeyboardOnclick(keyboardOnclick):

    def on_press(key):

        try:
            if((key.char in keyboardOnclick) == False) : 
                keyboardOnclick.append(key.char)
        except AttributeError:
            if((key in keyboardOnclick) == False) : 
                keyboardOnclick.append(key)

    def on_release(key):

        try:
            if(key.char in keyboardOnclick):
                keyboardOnclick.remove(key.char)
        except:
            if(key in keyboardOnclick):
                keyboardOnclick.remove(key)


    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()

#endregion

def CpseNullFunction():
    pass
    
class CRObj:

    crobj = []

    def __init__(self,crobj) -> None:
        self.crobj = crobj
#endregion

ccc = 0

class CpseEngine:

    """
    Cpse引擎基本类，实现Cpse的基本渲染操作
    """

    showCRO = [False]
    crobj = ""

    showFPS = False
    showFPSJG = []
    showFPSLast = 0
    showFPSPJ = 0

    lastframeScreen = []
    lastNullframeScreen = []
    last_frameScreen = []
    lastRenderingFrameSize = ()

    def __init__(self) -> None:
        threading.Thread(target=KeyboardOnclick,args=(keyboardOnclick,)).start()

    #region 渲染方法

    def RenderingFrame(self,frame:CpseFrame.CpseFrame) -> CRObj:
        global ccc
        """
        \n渲染一个Frame，返回渲染完成的CRObj
        \n(frame)被渲染的Frame
        """
        ccc = time.time()

        collisionSetList = [] #记录本次渲染已经产生碰撞的物体
        frameScreen = []
        tempFrame = []

        #region 渲染列表的创建

        if(self.lastRenderingFrameSize == frame.size):

            frameScreen = copy.deepcopy(self.lastNullframeScreen)

        else:

            append = frameScreen.append
            for i in range(frame.size[1]):  #创建渲染列表
                append([])
                append1 = frameScreen[i].append
                for j in range(frame.size[0]):
                    append1([])

            self.lastRenderingFrameSize = copy.deepcopy(frame.size)
            self.lastNullframeScreen = copy.deepcopy(frameScreen)

        #endregion

        for i in frame.frameObjList:  #读取Frame的CpseObj

            pos = i[1]
            anchorPoint = i[0].anchorPoint

            for j in i[0].objList:

                tempPos = [j[0] - anchorPoint[0] + pos[0],j[1] - anchorPoint[1] + pos[1],j[2]]

                if tempPos[0] >= frame.size[0]:
                    continue
                if tempPos[1] >= frame.size[1]:
                    continue
                if tempPos[0] < 0:
                    continue
                if tempPos[1] < 1:
                    continue

                if(len(j) == 3):
                    tempFrame.append([tempPos,i[0],0x07])
                else:
                    tempFrame.append([tempPos,i[0],j[3]])

        for i in tempFrame: #碰撞检测及最终加入列表

            if frameScreen[i[0][1]][i[0][0]] != []: #检查该位置是否已经有物体，如果有就进行碰撞检测

                aaaaa = set([i[1],frameScreen[i[0][1]][i[0][0]][1]]) in collisionSetList #判断本轮渲染是否已经触发过这两个物体的碰撞，防止多次触发
                if aaaaa == False:

                    if frameScreen[i[0][1]][i[0][0]][1].acceptCollision:
                        frameScreen[i[0][1]][i[0][0]][1].collisionFunction(target = i[1],selfObj = frameScreen[i[0][1]][i[0][0]][1])
                    if i[1].acceptCollision:
                        i[1].collisionFunction(target = frameScreen[i[0][1]][i[0][0]][1],selfObj = i[1])

                    collisionSetList.append(set([i[1],frameScreen[i[0][1]][i[0][0]][1]]))
                
            if isinstance(i[0][2],int):
                frameScreen[i[0][1]][i[0][0]] = (cpseRenderingFont[i[0][2]],i[1],i[2])
            else:
                frameScreen[i[0][1]][i[0][0]] = (i[0][2],i[1],i[2])

        #将渲染块按照颜色分类
        _frameScreen = []
        append = _frameScreen.append

        for i in frameScreen:

            append([])
            append1 = _frameScreen[-1].append

            if self.lastframeScreen != []:

                if frameScreen[len(_frameScreen) - 1] == self.lastframeScreen[len(_frameScreen) - 1]:
                    _frameScreen[len(_frameScreen) - 1] = self.last_frameScreen[len(_frameScreen) - 1]

                else:

                    for j in i:

                        if j == []:
                            if(len(_frameScreen[-1]) != 0):
                                if(_frameScreen[-1][-1][0] == 0x07):
                                    _frameScreen[-1][-1][1].append("  ")
                                else:
                                    append1([0x07,["  "]])
                            else:
                                append1([0x07,["  "]])
                        else:
                            if(len(_frameScreen[-1]) != 0):
                                if(_frameScreen[-1][-1][0] == j[2]):
                                    _frameScreen[-1][-1][1].append(j[0])
                                else:
                                    append1([j[2],[j[0]]])
                            else:
                                append1([j[2],[j[0]]])

            else:

                for j in i:

                    if j == []:
                        if(len(_frameScreen[-1]) != 0):
                            if(_frameScreen[-1][-1][0] == 0x07):
                                _frameScreen[-1][-1][1].append("  ")
                            else:
                                append1([0x07,["  "]])
                        else:
                            append1([0x07,["  "]])
                    else:
                        if(len(_frameScreen[-1]) != 0):
                            if(_frameScreen[-1][-1][0] == j[2]):
                                _frameScreen[-1][-1][1].append(j[0])
                            else:
                                append1([j[2],[j[0]]])
                        else:
                            append1([j[2],[j[0]]])

        self.last_frameScreen = list(_frameScreen)
        self.lastframeScreen = list(frameScreen)

        aaaa = time.time() - ccc
        return(CRObj(_frameScreen))

    def ShowCRObj(self,crobj:CRObj) -> bool:

        global ccc
        """\nShow已经渲染完成的Frame"""
        self.crobj = crobj

        buffer.switch()

        temp = ""
        cb = crobj.crobj
        for i in cb:

            for j in i: 

                bufferPrint(temp.join(j[1]),j[0])

            bufferPrint()

        stime = time.time() - ccc

        #region FPS显示
        if self.showFPS:

            self.showFPSJG.append(1/stime)
            if(len(self.showFPSJG) >= self.showFPSPJ): 
                fps = sum(self.showFPSJG) / len(self.showFPSJG)
                self.showFPSLast = fps
                self.showFPSJG = []
            else:
                fps = self.showFPSLast

            buffer.print()
            if fps != 0:
                buffer.print(str("{:.2f}".format(fps))+" fps")
        
        #endregion

        buffer.flash()

    def StartRenderingAndShowThread(self,frame,maxFPs = 200,update = CpseNullFunction):

        """
        \n启动CPSE渲染Frame并Show的进程
        \n(frame)被渲染的Frame
        \n(maxFPs)最大渲染帧率，决定每秒渲染的最大次数，默认100fps
        \n(updata)生命周期函数，每渲染帧会执行一次
        """

        self.showCRO[0] = True
        threading.Thread(target=CpseRendering,args=(self,frame,maxFPs,update)).start()

    def ExitRenderingAndShowThread(self):
        """\n停止渲染进程"""
        self.showCRO[0] = False

    #endregion

    #region 便捷功能

    def ObjectMoveKeyboardControlSet(self,cpseFrame:CpseFrame,obj:CpseObject,buttonTuple = ("w","s","a","d"),speed = 1):

        """
        \n用于快速创建对象键盘控制上下左右的方法
        \n(cpseFrame)控制的Frame
        \n(obj)控制的Object
        \n(buttonTuple)上下左右四个方向的控制按键，默认为wsad
        \n(speed)移动速度，默认为1
        """

        global keyboardOnclick

        if(buttonTuple[0] in keyboardOnclick):
            cpseFrame.MoveObject(obj,distance=speed,direction="u")
    
        if(buttonTuple[1] in keyboardOnclick):
            cpseFrame.MoveObject(obj,distance=speed,direction="d")

        if(buttonTuple[2] in keyboardOnclick):
            cpseFrame.MoveObject(obj,distance=speed,direction="b")

        if(buttonTuple[3] in keyboardOnclick):
            cpseFrame.MoveObject(obj,distance=speed,direction="f")

    def WaitRun(self,time:float,function):
        """
        \n等待指定时间后运行函数
        \n(time)等待时间
        \n(function)被运行的函数
        """
        threading.Thread(target=Run,args=(time,function)).start()
    
    def WaitRunRe(self,time:float,function):
        """
        \n每过去指定时间后运行函数
        \n(time)等待时间
        \n(function)被运行的函数
        """
        threading.Thread(target=RunRe,args=(time,function)).start()

    def GetKeyboardButtonDown(self,key) -> bool:
        """
        \n获取键盘按键是否按下
        \n(key)被获取的按键，字母按键提供字母字符串，控制按键调用Cpse的key变量
        """

        global keyboardOnclick

        if(key in keyboardOnclick):
            return True
        else:
            return False
    
    def ShowFPS(self,show:bool,interval = 10):
        """设置底端显示每interval帧平均FPS

        Args:
            show (bool): 是否显示
            interval (int): 更新FPS间隔帧，默认10帧
        """
        self.showFPS = show
        self.showFPSPJ = interval

    def LimitObjectExitFrame(self,frame:CpseFrame,obj:CpseObject,correction = 0):
        """限制Obj的中心点不得离开frame的边界，可通过修正值达到整体无法离开

        Args:
            frame (CpseFrame): obj所在的Frame
            obj (CpseObject): 被限制的obj
            correction (int): 修正偏移值，默认0
        """

        if frame.GetObjectPoint(obj)[0] >= frame.size[0] - correction:
            frame.SetObjectPoint(obj,(frame.size[0] - correction,frame.GetObjectPoint(obj)[1]))

        if frame.GetObjectPoint(obj)[0] <= frame.size[0] + correction:
            frame.SetObjectPoint(obj,(frame.size[0] + correction,frame.GetObjectPoint(obj)[1]))

        if frame.GetObjectPoint(obj)[1] <= frame.size[1] + correction:
            frame.SetObjectPoint(obj,(frame.GetObjectPoint(obj)[0],frame.size[1] + correction))

        if frame.GetObjectPoint(obj)[1] >= frame.size[1] - correction:
            frame.SetObjectPoint(obj,(frame.GetObjectPoint(obj)[0],frame.size[1] - correction))
    #endregion



class CpseFrame(CpseFrame.CpseFrame):
    pass

class CpseObject(CpseObject.CpseObject):
    pass

class CpsePhysics(CpsePhysics.CpsePhysics):
    pass
        
