from random import randint
from socket import MsgFlag
from nonebot.adapters.cqhttp import message
import os
from random import choice
from nonebot import on_command,on_keyword
from nonebot.adapters import Bot,Event
from nonebot.rule import to_me
from nonebot.typing import  T_State
from nonebot.adapters.cqhttp import Bot,Message,GroupMessageEvent

mes = on_keyword('夸')
@mes.handle()
async def mes_(bot:Bot,event:GroupMessageEvent,state:T_State):
    msg = str(event.get_message())
    if msg == '夸我':
        path = "./dataworlds/chp_am"
        path_ =  "./pic/chp_am"
        id = str(event.get_user_id())
        ins = sengs(path,path_,id)
    elif msg[0:2] == '夸他':
        try:
            path = "./dataworlds/chp_boys"
            path_ =  "./pic/chp_boys"
            id = str(event.get_message()).split('[')[1]
            id = id.split(']')[0]
            ins = sengs(path,path_,id)
        except:
            id = str(event.get_user_id())
            ins = try_ins(id)
    elif msg[0:2] == '夸她':
        try:
            path = "./dataworlds/chp_girls"
            path_ =  "./pic/chp_girls"
            id = str(event.get_message()).split('[')[1]
            id = id.split(']')[0]
            ins = sengs(path,path_,id)
        except:
            id = str(event.get_user_id())
            ins = try_ins(id)

    await bot.send(
        event=event,
        message=Message(ins)
        )

def sengs(path,path_,id):

    # 文字地址加载
    with open(path,"r", encoding="utf-8") as f:
        data = f.readlines()
        text = choice(data)
    # 图片地址加载
    path_list = os.listdir(path_ )
    path_random = choice(path_list)
    image_path = path_+'\\'+path_random

    # 构建@某人+文字
    at_ = "[CQ:at,qq={}]".format(id)
    msg = at_+'\n'+text
    msg = Message(msg)

    # 构建图片-------------------------------------------
    path_ = os.getcwd() # 方法用于返回当前工作目录
    path_ =  path_ + image_path
    mypath = 'file:///' + path_
    sst = message.MessageSegment.image(file= str(mypath))
    
    return (msg + sst)

def try_ins(id):
    # 图片地址加载
    path_ = "./pic/qaq"
    path_list = os.listdir(path_ )
    path_random = choice(path_list)
    image_path = path_+'\\'+path_random

    # 构建图片-------------------------------------------
    path_ = os.getcwd() # 方法用于返回当前工作目录
    path_ =  path_ + image_path
    mypath = 'file:///' + path_
    sst = message.MessageSegment.image(file= str(mypath))

    at_ = "[CQ:at,qq={}]".format(id)
    text = ['你需要夸的人呢?','可是，没有要夸的对象啊','请@你要夸的人']
    text = choice(text)

    msg = at_+'\n'+text
    msg = Message(msg)
    return (msg + sst)