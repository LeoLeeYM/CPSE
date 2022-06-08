基本说明

## 介绍

CPSE2是一款基于Python的Windows平台控制台画面渲染引擎，提供了丰富的游戏引擎功能，可以实现在Windows控制台高效率渲染画面以及开发游戏。

## 基本类

### CpseEngine

CpseEngine为CPSE2基本类，负责CPSE2的画面渲染，进行CPSE2的任何渲染操作均需要通过实例化后的CpseEngine进行操作，CpseEngine中亦包含许多实用方法为开发提供帮助。

| **Code**                   |   |
|----------------------------|---|
|  Cpse.CpseEngine()         |   |
| **参数列表**               |   |
| None                       |   |
| **示例Code**               |   |
|  cpse = Cpse.CpseEngine()  |   |

### CpseFrame

CpseFrame为CPSE2基本类，负责CPSE2的画面组建，所有CPSE2所渲染出的画面均为一个CpseFrame，可通过调整实例化后的CpseFrame改变画面。CpseFrame中可添加CpseObject，在CpseFrame中可以组织调整 CpseObject，最后提供给CpseEngine进行渲染。

| **Code**                          |       |             |
|-----------------------------------|-------|-------------|
|  Cpse.CpseFrame(frameSize:tuple)  |       |             |
| **参数列表**                      |       |             |
| frameSize                         | Tuple | Frame的宽高 |
| **Code**                          |       |             |
|  frame = Cpse.CpseFrame((50,50))  |       |             |

### CpseObject

CpseObject为CPSE2基本类，作为CPSE2画面的基本组成部分。

| **Code**                                                         |       |                  |
|------------------------------------------------------------------|-------|------------------|
|  Cpse.CpseObject(objList:list,anchorPoint:tuple)                 |       |                  |
| **参数列表**                                                     |       |                  |
| objList                                                          | List  | Object的组成列表 |
| anchorPoint                                                      | Tuple | Object的锚点     |
| **Code**                                                         |       |                  |
|  obj = Cpse.CpseObject([[0,0,0],[1,0,0],[0,1,0],[1,1,0]],(0,0))  |       |                  |

# 第一个CPSE2程序

让我们来制作我们的第一个CPSE2程序，将一个正方形渲染到控制台中。

下列展示的类方法按住Ctrl点击可跳转至方法介绍。

首先导入我们的CPSE2模块

| **Code**    |
|-------------|
| import Cpse |

然后我们实例化一个CpseEngine类，并且实例化一个宽高均为50的CpseFrame。

| **Code**                                                              |
|-----------------------------------------------------------------------|
| import Cpse  cpse = Cpse.CpseEngine() frame = Cpse.CpseFrame((50,50)) |

到这里我们就已经成功的完成了CPSE2的初始化，接下来就是要将我们的正方形作为一个CpseObject添加到我们的CpseFrame中。

CPSE的第0位渲染位即为一个正方形，所以我们直接实例化一个正方形CpseObject即可。

| **Code**                                                                                                                                 |
|------------------------------------------------------------------------------------------------------------------------------------------|
| import Cpse  cpse = Cpse.CpseEngine() frame = Cpse.CpseFrame((50,50))  obj = Cpse.CpseObject([[0,0,0], [0,1,0], [1,0,0], [1,1,0]],(0,0)) |

这一句代码中我们实例化了一个四个单位大小第0位渲染位图像的CpseObject，锚点是(0,0)，锚点即为Object在Frame中定位的坐标点，为相对坐标。

到此我们就完成了这个程序的一大半了，接下来我们需要将obj添加到frame中。

| **Code**                                                                                                                                                              |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| import Cpse  cpse = Cpse.CpseEngine() frame = Cpse.CpseFrame((50,50))  obj = Cpse.CpseObject([[0,0,0], [0,1,0], [1,0,0], [1,1,0]],(0,0)) frame.AddObject(obj,(10,10)) |

这一句代码中我们将obj加入到了frame中，初始位置为(10,10)

接下来只要将frame进行渲染就大功告成了！

| **Code**                                                                                                                                                                                                                                                 |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| import Cpse  cpse = Cpse.CpseEngine() 
frame = Cpse.CpseFrame((50,50))  
obj = Cpse.CpseObject([[0,0,0], [0,1,0], [1,0,0], [1,1,0]],(0,0)) 
frame.AddObject(obj,(10,10))  
cpse.[StartRenderingAndShowThread](#cpseenginestartrenderingandshowthread)(frame) |

通过最后一句代码启动cpse的渲染线程，将frame渲染并展示出来。

| **效果**                                        |
|-------------------------------------------------|
| ![](media/b9a2ff33f0a40891afb1e1d136b1d778.png) |

# 基本方法介绍

## CpseEngine

### CpseEngine.StartRenderingAndShowThread()

| **Code**                                                           |           |                                                |
|--------------------------------------------------------------------|-----------|------------------------------------------------|
|  CpseEngine.StartRenderingAndShowThread(frame,maxFPs,updata)       |           |                                                |
| **介绍**                                                           |           |                                                |
| 启动CpseEngine渲染Frame并Show的进程                                |           |                                                |
| **参数列表**                                                       |           |                                                |
| frame                                                              | CpseFrame | 被渲染的Frame                                  |
| maxFPs                                                             | int       | 最大渲染帧率；可空，默认100 Fps                |
| updata                                                             | function  | 更新函数，每渲染帧会执行一次；可空，默认无函数 |
| **Code**                                                           |           |                                                |
|  cpse.StartRenderingAndShowThread(frame,maxFPs=120,updata=updata)  |           |                                                |

### CpseEngine.ExitRenderingAndShowThread()

| **Code**                                  |
|-------------------------------------------|
|  CpseEngine.ExitRenderingAndShowThread()  |
| **介绍**                                  |
| 结束CpseEngine渲染Frame并Show的进程       |
| **Code**                                  |
|  cpse.ExitRenderingAndShowThread()        |

### CpseEngine.RenderingFrame()

| **Code**                                                                                                                                                                                                                                                                                                      |                                                         |               |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------|---------------|
|  CpseEngine.RenderingFrame(frame)                                                                                                                                                                                                                                                                             |                                                         |               |
| **介绍**                                                                                                                                                                                                                                                                                                      |                                                         |               |
| 渲染Frame，返回渲染完成后的CRObj对象，该对象为Frame的渲染结果。该方法仅渲染Frame，并不会显示到控制台，需使用CpseEngine.ShowCRObj才可以将CRObj显示到控制台。如非使用预渲染技术或自定义渲染过程，建议直接使用包含渲染和显示的[CpseEngine.StartRenderingAndShowThread()](#cpseenginestartrenderingandshowthread) |                                                         |               |
| **参数列表**                                                                                                                                                                                                                                                                                                  |                                                         |               |
| frame                                                                                                                                                                                                                                                                                                         | CpseFrame                                               | 被渲染的Frame |
| **返回值类型**                                                                                                                                                                                                                                                                                                |                                                         |               |
| CRObj                                                                                                                                                                                                                                                                                                         | 已完成渲染的Frame，可用CpseEngine.ShowCRObj显示到控制台 |               |
| **Code**                                                                                                                                                                                                                                                                                                      |                                                         |               |
|  crobj = cpse.RenderingFrame(frame)                                                                                                                                                                                                                                                                           |                                                         |               |

### CpseEngine.ShowCRObj()

| **Code**                                                                                                                                                                                                                  |       |                                                             |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|-------------------------------------------------------------|
|  CpseEngine.ShowCRObj(crobj)                                                                                                                                                                                              |       |                                                             |
| **介绍**                                                                                                                                                                                                                  |       |                                                             |
| 将已经完成渲染的Frame显示到控制台，该方法只会显示一帧，请配合循环使用。如非使用预渲染技术或自定义渲染过程，建议直接使用包含渲染和显示的[CpseEngine.StartRenderingAndShowThread()](#cpseenginestartrenderingandshowthread) |       |                                                             |
| **参数列表**                                                                                                                                                                                                              |       |                                                             |
| Crobj                                                                                                                                                                                                                     | CRObj | 已经渲染完成的Frame，可用CpseEngine.RenderingFrame渲染Frame |
| **Code**                                                                                                                                                                                                                  |       |                                                             |
|  cpse.ShowCRObj(crobj)                                                                                                                                                                                                    |       |                                                             |

### CpseEngine.ObjectMoveKeyboardControlSet()

| **Code**                                                                   |            |                                                           |
|----------------------------------------------------------------------------|------------|-----------------------------------------------------------|
|  CpseEngine.ObjectMoveKeyboardControlSet(cpseFrame,obj,buttonTuple,speed)  |            |                                                           |
| **介绍**                                                                   |            |                                                           |
| 快速创建CpseObject键盘控制上下左右移动                                     |            |                                                           |
| **参数列表**                                                               |            |                                                           |
| cpseFrame                                                                  | CpseFrame  | 被控制的CpseObject所在的Frame                             |
| obj                                                                        | CpseObject | 被控制的CpseObject                                        |
| buttonTuple                                                                | Tuple      | 上下左右四个方向的控制按键；可空，默认为("w","s","a","d") |
| speed                                                                      | int        | 移动速度；可空，默认为1                                   |
| **Code**                                                                   |            |                                                           |
|  cpse.ObjectMoveKeyboardControlSet(frame,obj)                              |            |                                                           |

### CpseEngine.WaitRun()

| **Code**                            |          |              |
|-------------------------------------|----------|--------------|
|  CpseEngine.WaitRun(time,function)  |          |              |
| **介绍**                            |          |              |
| 等待时间后执行函数                  |          |              |
| **参数列表**                        |          |              |
| time                                | float    | 等待的时间   |
| function                            | function | 被执行的函数 |
| **Code**                            |          |              |
|  cpse.WaitRun(2,Run)                |          |              |

### CpseEngine.WaitRunRe()

| **Code**                              |          |              |
|---------------------------------------|----------|--------------|
|  CpseEngine.WaitRunRe(time,function)  |          |              |
| **介绍**                              |          |              |
| 每过去指定时间后运行函数              |          |              |
| **参数列表**                          |          |              |
| time                                  | float    | 等待的时间   |
| function                              | function | 被执行的函数 |
| **Code**                              |          |              |
|  cpse.WaitRunRe(2,Run)                |          |              |

### CpseEngine.GetKeyboardButtonDown()

| **Code**                                                                      |     |                                                                 |
|-------------------------------------------------------------------------------|-----|-----------------------------------------------------------------|
|  CpseEngine.GetKeyboardButtonDown(key)                                        |     |                                                                 |
| **介绍**                                                                      |     |                                                                 |
| 获取按键是否按下                                                              |     |                                                                 |
| **参数列表**                                                                  |     |                                                                 |
| Key                                                                           | Any | 被获取的按键，字母按键提供字母字符串，控制按键调用Cpse的key变量 |
| **Code**                                                                      |     |                                                                 |
|  cpse.GetKeyboardButtonDown("j") cpse.GetKeyboardButtonDown(Cpse.key.ctrl_l)  |     |                                                                 |

## CpseFrame

### CpseFrame.AddObject()

| **Code**                       |            |                    |
|--------------------------------|------------|--------------------|
|  CpseFrame.AddObject(obj,pos)  |            |                    |
| **介绍**                       |            |                    |
| 用于往Frame中添加Object        |            |                    |
| **参数列表**                   |            |                    |
| obj                            | CpseObject | 被添加的CpseObject |
| pos                            | tuple      | obj在Frame中的位置 |
| **Code**                       |            |                    |
|  frame.AddObject(obj,(0,1))    |            |                    |

### CpseFrame.DelObject()

| **Code**                            |            |                    |
|-------------------------------------|------------|--------------------|
|  CpseFrame.AddObject(obj)           |            |                    |
| **介绍**                            |            |                    |
| 删除Frame中第一个同类型的CpseObject |            |                    |
| **参数列表**                        |            |                    |
| obj                                 | CpseObject | 被删除的CpseObject |
| **Code**                            |            |                    |
|  frame.DelObject(obj)               |            |                    |

### CpseFrame.SetObjectPoint()

| **Code**                            |            |                    |
|-------------------------------------|------------|--------------------|
|  CpseFrame.SetObjectPoint(obj,pos)  |            |                    |
| **介绍**                            |            |                    |
| 设置Object在Frame中的位置           |            |                    |
| **参数列表**                        |            |                    |
| obj                                 | CpseObject | 被设置的CpseObject |
| pos                                 | tuple      | 设置点             |
| **Code**                            |            |                    |
|  frame.SetObjectPoint(obj,(50,50))  |            |                    |

### CpseFrame.GetObjectPoint()

| **Code**                          |                    |                    |
|-----------------------------------|--------------------|--------------------|
|  CpseFrame.GetObjectPoint(obj)    |                    |                    |
| **介绍**                          |                    |                    |
| 获取Object在Frame中的位置         |                    |                    |
| **参数列表**                      |                    |                    |
| obj                               | CpseObject         | 被获取的CpseObject |
| **返回值类型**                    |                    |                    |
| tuple                             | CpseObject的所在点 |                    |
| **Code**                          |                    |                    |
|  pos = frame.GetObjectPoint(obj)  |                    |                    |

### CpseFrame.MoveObject()

| **Code**                                                 |            |                                                                  |
|----------------------------------------------------------|------------|------------------------------------------------------------------|
|  CpseFrame.MoveObject(obj,direction = "f",distance = 1)  |            |                                                                  |
| **介绍**                                                 |            |                                                                  |
| 移动Object                                               |            |                                                                  |
| **参数列表**                                             |            |                                                                  |
| obj                                                      | CpseObject | 被移动的CpseObject                                               |
| direction                                                | str        | 移动方向，提供str指定方向，默认为f（"f"前，"b"后，"u"上，"d"下） |
| distance                                                 | int        | 移动距离，默认为1                                                |
| **Code**                                                 |            |                                                                  |
|  frame.MoveObject(obj)                                   |            |                                                                  |

### CpseFrame.SetObjectLifeCycle()

| **Code**                                           |            |                                        |
|----------------------------------------------------|------------|----------------------------------------|
|  CpseFrame.SetObjectLifeCycle(obj,time,function)   |            |                                        |
| **介绍**                                           |            |                                        |
| 设置Object的生命周期，生命周期时间结束后会被销毁   |            |                                        |
| **参数列表**                                       |            |                                        |
| obj                                                | CpseObject | 被设置的CpseObject                     |
| time                                               | float      | 生命周期时间                           |
| function                                           | function   | 生命周期函数，生命周期结束后会执行一次 |
| **Code**                                           |            |                                        |
|  frame.SetObjectLifeCycle(Obj,1)                   |            |                                        |

## CpseObject

### CpseObject.SetObjcetList()

| **Code**                         |      |              |
|----------------------------------|------|--------------|
|  CpseObjct.SetObjectList(_list)  |      |              |
| **介绍**                         |      |              |
| 设置Object的列表                 |      |              |
| **参数列表**                     |      |              |
| \_list                           | list | 被设置的列表 |
| **Code**                         |      |              |
|  obj.SetObjectList(_list)        |      |              |

### CpseObject.GetObjcetList()

| **Code**                       |                  |
|--------------------------------|------------------|
|  CpseObjct.GetObjectList()     |                  |
| **介绍**                       |                  |
| 获取Object的ObjectList         |                  |
| **返回值类型**                 |                  |
| list                           | CpseObject的List |
| **Code**                       |                  |
|  \_list = obj.GetObjectList()  |                  |

### CpseObject.SetAnchorPoint()

| **Code**                                |       |              |
|-----------------------------------------|-------|--------------|
|  CpseObjct.SetAnchorPoint(anchorPoint)  |       |              |
| **介绍**                                |       |              |
| 设置Object的锚点                        |       |              |
| **参数列表**                            |       |              |
| anchorPoint                             | tuple | 被设置的锚点 |
| **Code**                                |       |              |
|  obj.SetAnchorPoint((1,1))              |       |              |

### CpseObject.GetAnchorPoint()

| **Code**                     |                  |
|------------------------------|------------------|
|  CpseObjct.GetAnchorPoint()  |                  |
| **介绍**                     |                  |
| 获取Object的锚点             |                  |
| **返回值类型**               |                  |
| tuple                        | CpseObject的锚点 |
| **Code**                     |                  |
|  pos = obj.GetAnchorPoint()  |                  |

### CpseObject.SetTag()

| **Code**                |     |        |
|-------------------------|-----|--------|
|  CpseObjct.SetTag(tag)  |     |        |
| **介绍**                |     |        |
| 设置Object的标签        |     |        |
| **参数列表**            |     |        |
| tag                     | str | 标签名 |
| **Code**                |     |        |
|  obj.SetTag("Player")   |     |        |

### CpseObject.GetTag()

| **Code**             |                  |
|----------------------|------------------|
|  CpseObjct.GetTag()  |                  |
| **介绍**             |                  |
| 获取Object的标签     |                  |
| **返回值类型**       |                  |
| str                  | CpseObject的标签 |
| **Code**             |                  |
|  tag = obj.GetTag()  |                  |

### CpseObject.SetKeyPoint()

| **Code**                            |       |            |
|-------------------------------------|-------|------------|
|  CpseObjct.SetKeyPoint(posTag,pos)  |       |            |
| **介绍**                            |       |            |
| 用于创建/更改Object的关键点         |       |            |
| **参数列表**                        |       |            |
| posTag                              | str   | 关键点标签 |
| pos                                 | tuple | 关键点坐标 |
| **Code**                            |       |            |
|  obj.SetKeyPoint("muzzle",(-1,-1))  |       |            |

### CpseObject.GetKeyPoint()

| **Code**                          |                        |            |
|-----------------------------------|------------------------|------------|
|  CpseObjct.GetKeyPoint(posTag)    |                        |            |
| **介绍**                          |                        |            |
| 获取Object的关键点                |                        |            |
| **参数列表**                      |                        |            |
| posTag                            | str                    | 关键点标签 |
| **返回值类型**                    |                        |            |
| tuple                             | CpseObject的关键点坐标 |            |
| **Code**                          |                        |            |
|  pos = obj.GetKeyPoint("muzzle")  |                        |            |

### CpseObject.AcceptCollisionStart()

| **Code**                                              |          |                                                                                                                 |
|-------------------------------------------------------|----------|-----------------------------------------------------------------------------------------------------------------|
|  CpseObjct.AcceptCollisionStart(trigger)              |          |                                                                                                                 |
| **介绍**                                              |          |                                                                                                                 |
| 启用Object的碰撞检测，每帧若触发碰撞会触发trigger函数 |          |                                                                                                                 |
| **参数列表**                                          |          |                                                                                                                 |
| trigger                                               | function | 触发函数，该函数需要设置接受下述参数："target"，用于获取被碰撞对象的CpseObject；"selfObj"，用于碰撞体获取自身。 |
| **Code**                                              |          |                                                                                                                 |
|  obj.AcceptCollisionStart(Trigger_Collision_Obj)      |          |                                                                                                                 |

### CpseObject.AcceptCollisionEnd()

| **Code**                         |
|----------------------------------|
|  CpseObjct.AcceptCollisionEnd()  |
| **介绍**                         |
| 关闭Object的碰撞检测             |
| **Code**                         |
|  obj.AcceptCollisionEnd()        |

### CpseObject.CopyObject()

| **Code**                                     |                      |
|----------------------------------------------|----------------------|
|  CpseObjct.GetKeyPoint(posTag)               |                      |
| **介绍**                                     |                      |
| 将该CpseObject复制，返回复制完成的CpseObject |                      |
| **返回值类型**                               |                      |
| CpseObject                                   | 复制完成的CpseObject |
| **Code**                                     |                      |
|  tempObj = Obj.CopyObject()                  |                      |

### CpseObject.TextToObjectList()

| **Code**                                                                                       |                    |                                            |
|------------------------------------------------------------------------------------------------|--------------------|--------------------------------------------|
|  CpseObjct.TextToObjectList(text,color = 0x07)                                                 |                    |                                            |
| **介绍**                                                                                       |                    |                                            |
| 静态方法。将Text转换为CpseObjectList，以此显示文字，暂不支持多行。部分半角符号会出现渲染错误。 |                    |                                            |
| **参数列表**                                                                                   |                    |                                            |
| posTag                                                                                         | str                | 被转换的文字                               |
| color                                                                                          | int                | 文字颜色，提供十六进制数，默认为黑色(0x07) |
| **返回值类型**                                                                                 |                    |                                            |
| list                                                                                           | 返回CpseObjectList |                                            |
| **Code**                                                                                       |                    |                                            |
|  obj = CpseObject(CpseObject.TextToObjectList(f"您的得分：{score}"),(0,0))                     |                    |                                            |

# 一个例程

一个飞机大战的游戏例程，实现了敌人移动、我方移动、我方攻击、攻击判定、被攻击判定、得分计算、胜负判定等功能，由CPSE2实现。

| **Code**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| import time import Cpse from Cpse import CpseEngine,CpseFrame,CpseObject import random  playerScore = 0 playerDie = False  \# CPSE基础组件初始化 cpse = CpseEngine() frame = CpseFrame((30,50))  attackInterval = 0 def Update():   \# region Player控制逻辑  global attackInterval  global playerScore  scoreObj.objList = CpseObject.TextToObjectList(f"您的得分：{playerScore}")   attackInterval += 1   cpse.ObjectMoveKeyboardControlSet(frame,playerObj)   if cpse.GetKeyboardButtonDown("j") and attackInterval % 4 == 0:   try:  tempPlayerBulletObj = playerBulletObj.CopyObject()  frame.AddObject(tempPlayerBulletObj,playerObj.GetKeyPoint("muzzle"))  frame.SetObjectLifeCycle(tempPlayerBulletObj,1)  except:  pass    try:    if frame.GetObjectPoint(playerObj)[0] \>= 28:  frame.SetObjectPoint(playerObj,(28,frame.GetObjectPoint(playerObj)[1]))   if frame.GetObjectPoint(playerObj)[0] \<= 1:  frame.SetObjectPoint(playerObj,(1,frame.GetObjectPoint(playerObj)[1]))   if frame.GetObjectPoint(playerObj)[1] \<= 1:  frame.SetObjectPoint(playerObj,(frame.GetObjectPoint(playerObj)[0],1))  if frame.GetObjectPoint(playerObj)[1] \>= 49:  frame.SetObjectPoint(playerObj,(frame.GetObjectPoint(playerObj)[0],49))  except:  pass   PlayerBulletMove()  \# endregion   EnemyMove()  \# region 触发器函数  def Trigger_Collision_enemyObj(target,selfObj):  if target.GetTag() == "Player":  try:  frame.DelObject(target)  frame.DelObject(scoreObj)   global playerScore  showTipObj = CpseObject(CpseObject.TextToObjectList("您已经失败，最终得分：{0}".format(playerScore),4),(0,0))  frame.AddObject(showTipObj,(9,25))   global playerDie  playerDie = True   except:  pass  def Trigger_Collision_playerBulletObj(target,selfObj):  if target.GetTag() == "Enemy":  frame.DelObject(target)  global playerScore  playerScore += 1  \# endregion  \# region 生命周期函数  def PlayerBulletMove():  for i in frame.frameObjList:  if i[0].GetTag() == "PlayerBullet":  frame.MoveObject(i[0],distance=1,direction="u")  def EnemyBulletMove():  for i in frame.frameObjList:  if i[0].GetTag() == "EnemyBullet":  frame.MoveObject(i[0],distance=1,direction="d")  enemyMoveInterval = 0 def EnemyMove():  global enemyMoveInterval  enemyMoveInterval += 1  if enemyMoveInterval % 1 == 0:  for i in frame.frameObjList:  if i[0].GetTag() == "Enemy":  frame.MoveObject(i[0],distance=1,direction="d")   if(frame.GetObjectPoint(i[0])[1] \>= 60): frame.DelObject(i[0])  \# endregion  \# region Object组件初始化  playerObj = CpseObject([[0, 0, 0, 7], [0, -1, 1, 15], [-1, 0, 3, 3], [1, 0, 3, 3], [0, 0, 0, 15]],(0,0)) playerObj.SetKeyPoint("muzzle",(0,-1))  playerObj.SetTag("Player")  playerBulletObj = CpseObject([[0, 0, 4, 11]],(0,0)) playerBulletObj.SetTag("PlayerBullet") playerBulletObj.AcceptCollisionStart(Trigger_Collision_playerBulletObj)  enemyObj = CpseObject([[0, 0, 0, 7], [0, 1, 7, 15], [-1, 0, 3, 4], [1, 0, 3, 4]],(0,0)) enemyObj.SetKeyPoint("muzzle_l",(-1,-1)) enemyObj.SetKeyPoint("muzzle_r",(1,-1)) enemyObj.SetTag("Enemy") enemyObj.AcceptCollisionStart(Trigger_Collision_enemyObj)  scoreObj = CpseObject(CpseObject.TextToObjectList(f"您的得分：{playerScore}"),(0,0))  \#endregion  \# 初始化 frame.AddObject(playerObj,(14,45)) frame.AddObject(scoreObj,(1,1))  cpse.StartRenderingAndShowThread(frame,update=Update)  time.sleep(2) def CreatEnemy():  if playerDie != True:  frame.AddObject(enemyObj.CopyObject(),(random.randint(1,29),3)) cpse.WaitRunRe(0.025,CreatEnemy)  |
