from nonebot import on_command
from nonebot.adapters import Bot,Event
from nonebot.rule import to_me
from nonebot.typing import  T_State
from nonebot.adapters.cqhttp import Bot,Message,GroupMessageEvent

test = on_command('test',rule = to_me()) # 事件响应器

@test.handle()  # 装饰起来
async def h_r(bot:Bot,event:GroupMessageEvent,state:T_State):
    id = str(event.get_user_id())
    at_ = "[CQ:at,qq={}]".format(id)
    msg = at_+'在呢在呢'
    msg = Message(msg)
    await test.finish(msg)
'''
https://www.bilibili.com/video/BV13h411B7eN  视频
kaptreebot的GitHub:https://github.com/MangataTS/kaptreebot
priority=2 优先度 数字越小，等级越高，创建响应器的参数，优先级可以对相同触发的命令的触发
GroupMessageEvent 监听群消息
state:dict 未知
await bot.send(
    event = event,
    message = "hello master"
    )

await bot.go_api终结点

on_command 全匹配   aliases={'早安'}可以再添加
on_keyword 关键字匹配
on_message 消息全匹配，智能机器人遍历
mangata.ltd 作者api

'''
'''
https://www.bilibili.com/video/BV1JK4y1D7kX

return await bot.call_api('gocqhttpapi_终结点', **{
    'message':'消息内容'
    'group_id':'群id' # 一定要注意goapi的格式类型
})

bot = nonebot.get_bot()['32163546']  # 多qq下调用指定qq发送消息

premission 权限模块可以给一些任务制作权限或者管理员or群主


'''