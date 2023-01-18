from nonebot import on_keyword,on_message
from nonebot.rule import to_me
from nonebot.adapters.onebot.v11.message import MessageSegment
from nonebot.adapters.onebot.v11 import GROUP
from .data import atri_text
from .data import V_PATH
import random

call = on_keyword(['亚托莉','アトリ','atri'], priority=1, block=True)
call2 = on_message(rule=to_me(),permission=GROUP, priority=1)

@call.handle()
async def _():
    await call.finish('haihai~~~~(≧▽≦)')

@call2.handle()
async def _():
    voice = random.choice(atri_text)["o"]
    # text = re.findall("(.*).mp3", voice)[0]
    text = voice.rstrip(".mp3")
    print(f"voice = {voice},text = {text}")
    await call2.send(MessageSegment.record(f"file:///{V_PATH}" + str(voice)))
    await call2.finish(text)
    # await call.finish('haihai~~~~(≧▽≦)')
