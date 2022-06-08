import time
import Cpse
from Cpse import CpseEngine,CpseFrame,CpseObject
import random

playerScore = 0
playerDie = False

# CPSE基础组件初始化
cpse = CpseEngine()
frame = CpseFrame((30,50))

attackInterval = 0
def Update():

    # region Player控制逻辑
    global attackInterval
    global playerScore
    scoreObj.objList = CpseObject.TextToObjectList(f"您的得分：{playerScore}")



    attackInterval += 1

    cpse.ObjectMoveKeyboardControlSet(frame,playerObj)

    if cpse.GetKeyboardButtonDown("j") and attackInterval % 3 == 0:

        try:
            tempPlayerBulletObj = playerBulletObj.CopyObject()
            frame.AddObject(tempPlayerBulletObj,playerObj.GetKeyPoint("muzzle"))
            frame.SetObjectLifeCycle(tempPlayerBulletObj,1)
        except:
            pass
    
    try:
        
        if frame.GetObjectPoint(playerObj)[0] >= 28:
            frame.SetObjectPoint(playerObj,(28,frame.GetObjectPoint(playerObj)[1]))

        if frame.GetObjectPoint(playerObj)[0] <= 1:
            frame.SetObjectPoint(playerObj,(1,frame.GetObjectPoint(playerObj)[1]))

        if frame.GetObjectPoint(playerObj)[1] <= 1:
            frame.SetObjectPoint(playerObj,(frame.GetObjectPoint(playerObj)[0],1))
        if frame.GetObjectPoint(playerObj)[1] >= 49:
            frame.SetObjectPoint(playerObj,(frame.GetObjectPoint(playerObj)[0],49))
    except:
        pass

    PlayerBulletMove()
    # endregion

    EnemyMove()

# region 触发器函数

def Trigger_Collision_enemyObj(target,selfObj):
    if target.GetTag() == "Player":
        try:
            frame.DelObject(target)
            frame.DelObject(scoreObj)

            global playerScore
            showTipObj = CpseObject(CpseObject.TextToObjectList("您已经失败，最终得分：{0}".format(playerScore),4),(0,0))
            frame.AddObject(showTipObj,(9,25))

            global playerDie
            playerDie = True

        except:
            pass

def Trigger_Collision_playerBulletObj(target,selfObj):
    if target.GetTag() == "Enemy":
        frame.DelObject(target)
        global playerScore
        playerScore += 1

# endregion

# region 生命周期函数

def PlayerBulletMove():
    for i in frame.frameObjList:
        if i[0].GetTag() == "PlayerBullet":
            frame.MoveObject(i[0],distance=1,direction="u")

def EnemyBulletMove():
    for i in frame.frameObjList:
        if i[0].GetTag() == "EnemyBullet":
            frame.MoveObject(i[0],distance=1,direction="d")

enemyMoveInterval = 0
def EnemyMove():
    global  enemyMoveInterval
    enemyMoveInterval += 1
    if enemyMoveInterval % 1 == 0:
        for i in frame.frameObjList:
            if i[0].GetTag() == "Enemy":
                frame.MoveObject(i[0],distance=1,direction="d")

                if(frame.GetObjectPoint(i[0])[1] >= 60): frame.DelObject(i[0])

# endregion

# region Object组件初始化

playerObj = CpseObject([[0, 0, 0, 7], [0, -1, 1, 15], [-1, 0, 3, 3], [1, 0, 3, 3], [0, 0, 0, 15]],(0,0))
playerObj.SetKeyPoint("muzzle",(0,-1))

playerObj.SetTag("Player")

playerBulletObj = CpseObject([[0, 0, 4, 11]],(0,0))
playerBulletObj.SetTag("PlayerBullet")
playerBulletObj.AcceptCollisionStart(Trigger_Collision_playerBulletObj)

enemyObj = CpseObject([[0, 0, 0, 7], [0, 1, 7, 15], [-1, 0, 3, 4], [1, 0, 3, 4]],(0,0))
enemyObj.SetKeyPoint("muzzle_l",(-1,-1))
enemyObj.SetKeyPoint("muzzle_r",(1,-1))
enemyObj.SetTag("Enemy")
enemyObj.AcceptCollisionStart(Trigger_Collision_enemyObj)

scoreObj = CpseObject(CpseObject.TextToObjectList(f"您的得分：{playerScore}"),(0,0))

#endregion

# 初始化
frame.AddObject(playerObj,(14,45))
frame.AddObject(scoreObj,(1,1))

cpse.StartRenderingAndShowThread(frame,update=Update)

time.sleep(2)
def CreatEnemy():
    if playerDie != True:
        frame.AddObject(enemyObj.CopyObject(),(random.randint(1,29),3))
cpse.WaitRunRe(0.035,CreatEnemy)

