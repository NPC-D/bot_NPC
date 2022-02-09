from nonebot import on_command
from nonebot.adapters import Bot,Event
from nonebot.rule import to_me
from nonebot.typing import  T_State
from nonebot.adapters.cqhttp import Bot,Message,GroupMessageEvent
from pydantic.errors import NumberNotGeError
import requests
from random import randint
from nonebot.adapters.cqhttp import message
import requests

# 问题：服务器网络不好导致
# 原因：1.网络质量 2.没忘
# 解决：1.多关键字解决多图床 2.时间判断

welfares = on_command('r18')
@welfares.handle()  # 装饰起来
async def h_r(bot:Bot,event:GroupMessageEvent,state:T_State):
    ins = welhxh()
    sst = message.MessageSegment.image(file = ins)#(file = str(mypath))
    await bot.send(
        event=event,
        message=Message(sst)
        )
def welhxh():
    ins = requests.get('https://api.nmb.show/xiaojiejie1.php') # 这是真人福利姬
    if str(ins) == '<Response [200]>':
        return ins.content
    else:
        return(welhxh_1())
        
def welhxh_0():
    ins = requests.get('https://acg.yanwz.cn/api.php') # 这是个二次元接口
    return ins.content

def welhxh_1():
    ins = requests.get('https://api.vvhan.com/api/mobil.girl') # 真人美女
    if str(ins) == '<Response [200]>':
        return ins.content
    else:
        return(welhxh_0())