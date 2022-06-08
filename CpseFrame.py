import imp
import CpseObject
import threading
import time

def ObjLifeCycle(frameSelf,_time,obj,fun):
    time.sleep(_time)
    frameSelf.DelObject(obj)
    fun()

def CpseNullFunction():
    pass

class CpseFrame:

    """
    Cpse的基本组件，用于预制Cpse画面
    """

    frameObjList = []
    size = ()

    def __init__(self,frameSize:tuple):

        """
        \n(frameSize)Frame的大小 -> (w,h)
        """

        self.size = frameSize

    def AddObject(self,obj:CpseObject.CpseObject,pos:tuple):

        """
        \n用于往Frame中添加Object
        \n(obj)CpseObject对象
        \n(pos)CpseObject在Frame中的位置
        """
        self.frameObjList.append([obj,pos])

    def DelObject(self,obj:CpseObject.CpseObject):

        """
        \n用于删除Frame中的Object
        \n删除Frame中第一个同类型的CpseObject
        """

        for i in range(len(self.frameObjList)):
            if self.frameObjList[i][0] == obj : 
                del self.frameObjList[i]
                break


    def SetObjectPoint(self,obj:CpseObject.CpseObject,pos:tuple):
        """设置Object的位置

        Args:
            obj (CpseObject.CpseObject): 被设置的对象
            pos (tuple): 设置到的点
        """
        for i in range(len(self.frameObjList)):
            if self.frameObjList[i][0] == obj : 
                self.frameObjList[i][1] = pos
                obj.nowPoint = self.GetObjectPoint(obj)

    def GetObjectPoint(self,obj:CpseObject.CpseObject) -> tuple:

        """获取Object的位置

        Args:
            obj (CpseObject.CpseObject): 被获取的对象

        Returns:
            tuple: 获取到的位置元组
        """
        
        for i in range(len(self.frameObjList)):
            if self.frameObjList[i][0] == obj : 
                return self.frameObjList[i][1]     
    
    def MoveObject(self,obj:CpseObject.CpseObject,direction = "f",distance = 1):

        """
        \n移动Object
        \n(obj)CpseObject对象
        \n(direction)移动方向，提供str指定方向，默认为f（"f"前，"b"后，"u"上，"d"下）
        \n(distance)移动距离，默认为1
        """

        for i in range(len(self.frameObjList)):
            if direction == "f":
                if self.frameObjList[i][0] == obj : self.frameObjList[i][1] = (self.frameObjList[i][1][0] + distance,self.frameObjList[i][1][1])
            elif direction == "b":
                if self.frameObjList[i][0] == obj : self.frameObjList[i][1] = (self.frameObjList[i][1][0] - distance,self.frameObjList[i][1][1])
            elif direction == "u":
                if self.frameObjList[i][0] == obj : self.frameObjList[i][1] = (self.frameObjList[i][1][0],self.frameObjList[i][1][1] - distance)
            elif direction == "d":
                if self.frameObjList[i][0] == obj : self.frameObjList[i][1] = (self.frameObjList[i][1][0],self.frameObjList[i][1][1] + distance)

        obj.nowPoint = self.GetObjectPoint(obj)

    def SetObjectLifeCycle(self,obj:CpseObject.CpseObject,time:float,function = CpseNullFunction):
        """
        \n设置Object的生命周期，生命周期时间结束后会被销毁
        \n(obj)被设置的Object
        \n(time)时间
        \n(function)生命周期函数，生命周期结束后会执行一次
        """
        threading.Thread(target=ObjLifeCycle,args=(self,time,obj,function)).start()

    #def SetObjLifeCycle()