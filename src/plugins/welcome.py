from nonebot import on_notice
from nonebot.adapters import Bot,Event
from nonebot.rule import to_me
from nonebot.typing import  T_State
from nonebot.adapters.cqhttp import Bot,Message,GroupIncreaseNoticeEvent,GroupDecreaseNoticeEvent

welcom = on_notice()   # 消息相应器
@welcom.handle()
async def welcom_(bot: Bot,event:GroupIncreaseNoticeEvent,state: T_State): # 这里定义event定义了不同的事件响应
    user = event.get_user_id()
    at_ = "[CQ:at,qq={}]".format(user)
    msg = at_ +'\n欢迎新进群的小伙伴:\n来了就别想走了哦'
    msg = Message(msg)
    await welcom.finish(message=msg)
    
@welcom.handle()
async def welcom_bye(bot: Bot,event:GroupDecreaseNoticeEvent,state: T_State):
    user = event.get_user_id()
    at_ = "[CQ:at,qq={}]".format(user)
    msg = at_ +'\n/(ToT)/~~\n又一位朋友离我们而去'
    msg = Message(msg)
    await welcom.finish(message=msg)