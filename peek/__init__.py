from PIL import ImageGrab,Image,ImageFilter
from nonebot import on_command
from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot.params import CommandArg, Message
import io
import time

t1 = -200
peek = on_command('peek',priority=1, block=True)
@peek.handle()
async def _(msg: Message = CommandArg()):
    global t1
    t2 = time.time()
    print('当前时间戳：',t2,' 差值：',t2 - t1)
    if((t2 - t1) < 50):
        await peek.finish('peek过于频繁！')
    t1 = t2
    img = ImageGrab.grab(bbox=(0, 0, 1920, 1080))
    img = img.filter(ImageFilter.GaussianBlur(radius=2))
    msg = MessageSegment.image(img2Byte(img))
    await peek.finish(msg)

def img2Byte(img:Image) -> bytes:
    imgByte=io.BytesIO()
    img.save(imgByte,format='JPEG')
    byte_res=imgByte.getvalue()
    return byte_res
