class CpseObject:

    """
    Cpse的基本组件，一个物体
    """
    objTag = ""
    
    objList = []
    anchorPoint = ()

    nowPoint = (0,0)

    acceptCollision = False
    collisionFunction = None

    keyPoint = {}

    def __init__(self,objList:list,anchorPoint:tuple):

        """
        \n(objList)提供一个CpseObjcet组件的基础渲染坐标列表以及渲染符号id -> [[x,y,id],[x1,y1,id]...]
        \n(anchorPoint)提供一个CpseObjcet组件的渲染锚点 -> (x,y)
        """

        self.objList = objList
        self.anchorPoint = anchorPoint

    #region 数据GetSet操作

    def GetObjectList(self) -> list:
        return self.objList

    def SetObjectList(self,_list:list):
        """
        \n设置Object的列表
        \n(_list)被设置的列表
        """
        self.objList = _list

    def GetAnchorPoint(self) -> tuple:
        return self.anchorPoint

    def SetAnchorPoint(self,anchorPoint:tuple):
        """
        \n设置Object的锚点
        \n(anchorPoint)锚点坐标
        """
        self.anchorPoint = anchorPoint

    def SetTag(self,tag:str):
        """
        \n设置Object的标签
        \n(tag)标签名
        """
        self.objTag = tag

    def GetTag(self) -> str:
        """
        \n获取Object的标签
        """
        return self.objTag

    def SetKeyPoint(self,posTag:str,pos:tuple):
        """
        \n用于创建/更改Object的关键点
        \n(posTag)关键点标签，每个posTag对应一个唯一的关键点
        \n(pos)关键点坐标
        """
        self.keyPoint[posTag] = pos

    def GetKeyPoint(self,posTag:str) -> tuple:
        """
        \n获取Object的关键点
        \n(posTag)关键点标签，每个posTag对应一个唯一的关键点
        """
        tempPos = [self.keyPoint[posTag][0] - self.anchorPoint[0] + self.nowPoint[0],self.keyPoint[posTag][1] - self.anchorPoint[1] + self.nowPoint[1]]

        return tempPos
    
    #endregion

    #region 碰撞实现
    def AcceptCollisionStart(self,trigger):

        """
        \n启用Object的碰撞检测，每帧若触发碰撞会触发trigger函数
        \n(trigger)碰撞触发函数，该函数需要设置接受下述参数："target"，用于获取被碰撞对象的CpseObject；"selfObj"，用于碰撞体获取自身
        """

        self.acceptCollision = True
        self.collisionFunction = trigger

    def AcceptCollisionEnd(self,trigger):

        """
        \n关闭Object的碰撞检测
        """

        self.acceptCollision = False
        self.collisionFunction = None
    #endregion

    def CopyObject(self):

        """将该CpseObject复制，返回复制完成的CpseObject"""
        temp = CpseObject(self.objList,self.anchorPoint)
        temp.acceptCollision = self.acceptCollision
        temp.collisionFunction = self.collisionFunction
        temp.objTag = self.objTag
        temp.keyPoint = self.keyPoint

        return temp

    def TextToObjectList(text:str,color = 0x07) -> list:

        """将Text转换为CpseObjectList，以此显示文字，暂不支持多行。部分半角符号会出现渲染错误。

        Args:
            text (str): 被转换的文字
            color (hex): 文字颜色，提供十六进制数，默认为黑色(0x07)

        Returns:
            list: 返回CpseObjectList
        """

        enChar = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890,./?;'[]{}\\|+=-_()!@#$%^&*~`<>"

        js = 0
        for i in text:
            if i in enChar: js += 1
            else: js += 2

        rtList = [[0,0,text,color]]

        if js % 2 == 0:
            for i in range((js//2) - 1):
                rtList.append([i + 1,0,""])
        else:
            for i in range((js//2)):
                rtList.append([i + 1,0,""])

        return rtList

