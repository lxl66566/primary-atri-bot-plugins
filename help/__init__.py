from nonebot import on_command
from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot.params import CommandArg, Message
from pathlib import Path
import os
# from io import BytesIO
# from PIL import Image
# import base64

help = on_command('help',aliases = {'帮助'}, priority=1, block=True)

@help.handle()
async def _(msg: Message = CommandArg()):
    # img = Image.open(os.path.dirname(__file__) + '\\help.png')
    msg = MessageSegment.image(Path(os.path.dirname(__file__) + '\\help.png'))
    await help.finish(msg)
    # temp = image_to_base64(img)
    # await help.finish(Message([{
    #     "type": "image",
    #     "data": {
    #         "file": f"base64://{str(temp, encoding='utf-8')}"
    #     }
    # }]))

# def image_to_base64(img, format='PNG'):
#     output_buffer = BytesIO()
#     img.save(output_buffer, format)
#     byte_data = output_buffer.getvalue()
#     base64_str = base64.b64encode(byte_data)
#     return base64_str