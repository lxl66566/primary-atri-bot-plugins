from nonebot import on_command
import random
from nonebot.params import CommandArg, Message

__plugin_name__ = 'roll'
__plugin_usage__ = r"""
roll点
\
\roll  {点数} 这是个可选的参数 默认是100
"""

rd = on_command("rd", priority=1, block=True)
rf = on_command("rf", priority=1, block=True)


@rd.handle()
async def handle_first_receive(msg: Message = CommandArg()):
    try:
        args = list(map(int, msg.extract_plain_text().split()))  # 首次发送命令时跟随的参数
    except ValueError:
        await rd.finish("请输入空格隔开的两个/三个数字！")
        return
    if not 2 <= len(args) <= 3:
        await rd.finish("请输入空格隔开的两个/三个数字！")
    elif len(args) == 2:
        await rd.finish(str(random.randint(args[0], args[1])) + f'  in[{args[0]},{args[1]}]')
    else:
        s = ''
        for i in range(args[2]):
            s += str(random.randint(args[0], args[1]))
            s += ' '
        await rd.finish(s + f' in[{args[0]},{args[1]}]')


@rf.handle()
async def handle_first_receive(msg: Message = CommandArg()):
    try:
        args = list(map(float, msg.extract_plain_text().split()))  # 首次发送命令时跟随的参数
    except ValueError:
        await rd.finish("请输入空格隔开的两个/三个数字！")
        return
    if len(args) not in (0, 2, 3):
        await rd.finish("请输入空格隔开的两个/三个数字！")
    elif len(args) == 0:
        await rd.finish(str(random.random()) + f' in[0,1]')
    elif len(args) == 2:
        await rd.finish(str(random.uniform(args[0], args[1])) + f'  in[{args[0]},{args[1]}]')
    else:
        times = str(int(args[2]))
        if not times.isdigit():
            await rd.finish('随机次数应是正整数！')
        s = ''
        for i in range(int(times)):
            s += str(random.uniform(args[0], args[1]))
            s += '\n'
        await rd.finish(s + f'\nin[{args[0]},{args[1]}]')
