from nonebot import on_command
from nonebot.adapters import Bot,Event
from nonebot.rule import to_me
from nonebot.typing import  T_State
from nonebot.adapters.cqhttp import Bot,Message,GroupMessageEvent
from pydantic.errors import NumberNotGeError
import requests
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
from io import BytesIO
import datetime
import json
from random import randint
import time
from nonebot.adapters.cqhttp import message
import os
from Mornings import *

Sign_in = on_command('签到')
@Sign_in.handle()  

async def in_(bot:Bot,event:GroupMessageEvent,state:T_State):
    # ---------------------------------------------------------------

    # 预加载json数据
    data = json.load(open("./config.json", encoding='utf-8'))
    qlist = list(data .keys())
    # 基础数据
    id = str(event.get_user_id())
    q_nickname=str(event.sender.nickname) 
    times= event.time  # 这里是nonebot接受消息之后产生的时间

    # ----------------------没什么屁事不要动他们👆--------------------

    # 判断存在
    if id not in qlist:
        # 初始化数据
        # 时间戳，签总数：1，硬币：5,好感度：6,连续签到树：1
        data[id]= {"time_stamp":1637464516,"Sign_in":0,"Coin":0,"Favorability":0,"Signs":1,"Lukc":0} 
        # 写入
        with open("config.json",'w',encoding='utf8')as fp:
            json.dump(data,fp,ensure_ascii=False)

        # 启动send函数
        q_q(id,q_nickname,times)
    else:
        # json时间数据
        timeStamp = data[id]["time_stamp"] # 拿到时间戳
        dateArray = datetime.datetime.fromtimestamp(timeStamp)
        otherStyleTime = dateArray.strftime("%Y-%m-%d")
        time0 = datetime.datetime.strptime(otherStyleTime,"%Y-%m-%d") # 这里将时间戳转化
        # 此刻时间数据
        now = datetime.datetime.now()
        otherStyleTime = now.strftime("%Y-%m-%d")
        now_time = datetime.datetime.strptime(otherStyleTime,"%Y-%m-%d")
        # 时间区间一天
        One_day = datetime.timedelta(seconds=86400) # 这里限定时间为一天
        
        if now_time-time0 >= One_day:
            if now_time-time0 > 2*One_day:
                data[id]["Signs"] = 0
                with open("config.json",'w',encoding='utf8')as fp:
                    json.dump(data,fp,ensure_ascii=False)
            q_q(id,q_nickname,times)
            
        else:
            goodbay(q_nickname,id)
            # -----------------------------发送图片-----------------------------------
            path_ = os.getcwd() # 方法用于返回当前工作目录
            path_ =  path_ +'\ph1.png'
            mypath = 'file:///' + path_
            sst = message.MessageSegment.image(file= str(mypath))
            await bot.send(
                event=event,
                message=Message(sst)
                )
            os.remove(".\ph1.png")
            

    # -----------------------------发送图片-----------------------------------
    path_ = os.getcwd() # 方法用于返回当前工作目录
    path_ =  path_ +'\ph.png'
    mypath = 'file:///' + path_
    sst = message.MessageSegment.image(file= str(mypath))
    await bot.send(
        event=event,
        message=Message(sst)
        )
    # -----------------------------发送图片-----------------------------------
    path_ = os.getcwd() # 方法用于返回当前工作目录
    path_ =  path_ +'\ph0.png'
    mypath = 'file:///' + path_
    sst = message.MessageSegment.image(file= str(mypath))
    await bot.send(
        event=event,
        message=Message(sst)
        )
    os.remove(".\ph.png")
    os.remove(".\ph0.png")
    
def q_q(id,q_nickname,times):

    # 更改数据内容------------------------------------------------------
    data = json.load(open("./config.json", encoding='utf-8'))
    
    # 后台数据写入------------------------------------------------------
    luck = randint(0,10)

    if luck > 7:
        lucks = 2*(8+luck*(int(luck/2)))
        data[id]["Favorability"] += lucks # 两倍幸运
    elif luck >= 9:
        lucks = 3*(8+luck*(int(luck/2)))
        data[id]["Favorability"] += lucks # 三倍幸运
    else:
        lucks = 6+luck*(int(luck/2))
        data[id]["Favorability"] += lucks # 幸运值
    data[id]["Luck"] = luck
    data[id]["Sign_in"] += 1
    data[id]["Signs"] += 1
    data[id]["Coin"] += luck*(int(luck/2))+luck # 硬币
    data[id]["time_stamp"] = times
    with open("config.json",'w',encoding='utf8')as fp:
        json.dump(data,fp,ensure_ascii=False)
    # -----------------------------------------------------------------

    # 时间判断这里在一些特殊情况下，可能出现时间上的错位bug
    now_time = datetime.datetime.now()

    # ---------------------------------------时间判断区块-----------------------------------------------------------
    #start_work_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '7:00', '%Y-%m-%d%H:%M')
    #end_work_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '9:00', '%Y-%m-%d%H:%M')
    
    start_morning_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '5:00', '%Y-%m-%d%H:%M')
    end_morning_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '11:00', '%Y-%m-%d%H:%M')

    start_noon_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '11:00', '%Y-%m-%d%H:%M')
    end_noon_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '14:00', '%Y-%m-%d%H:%M')

    start_afternoon_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '14:00', '%Y-%m-%d%H:%M')
    end_afternoon_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '19:00', '%Y-%m-%d%H:%M')

    start_evening_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '19:00', '%Y-%m-%d%H:%M')
    end_evening_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '23:00', '%Y-%m-%d%H:%M')
    
    hallo(q_nickname,id,lucks,luck)

    if start_morning_time < now_time < end_morning_time:
        Morning(q_nickname,id,times,luck)
    elif start_noon_time < now_time < end_noon_time:
        noon(q_nickname,id,times,luck)
    elif start_afternoon_time < now_time < end_afternoon_time:
        Afternoons(q_nickname,id,times,luck)
    elif start_evening_time < now_time < end_evening_time:
        Evening(q_nickname,id,times,luck)  
    else:
        Nights(q_nickname,id,times,luck)

    
    

    # ---------------------------------------------------------------------------------------------------------------
