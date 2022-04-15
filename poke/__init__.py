from webbrowser import get
from nonebot.adapters.onebot.v11 import Message, Event, OneBotAdapterException
from nonebot import on_notice,on_command
from nonebot.adapters.onebot.v11.message import MessageSegment
from nonebot.params import CommandArg, Message
from nonebot.log import logger
import random
import os,json
from .sql import get_data,add_data,update_data

async def _group_poke(event: Event) -> bool:
    value = (event.post_type == "notice" and event.get_event_name() == "notice.notify.poke" and event.__getattribute__(
        'target_id') == event.self_id)
    return value

poke = on_notice(rule=_group_poke, priority=1, block=True)
change_language = on_command('select',aliases = {'选择','choose'},priority=1, block=True)
debug1 = on_command('print_hole_database',priority=1, block=True)

@poke.handle()
async def _(event: Event):
    eng = os.path.dirname(__file__) + '\\words\\' + random.choice(os.listdir(os.path.dirname(__file__) + '\\words'))
    jp = os.path.dirname(__file__) + '\\nihonngo_for_final.json'
    user = str(event.get_user_id())
    data = get_data()
    choice_ = eng
    for uid,choose in data:
        if user == str(uid):
            if choose == '日语':
                choice_ = jp
            elif choose == '英语':
                choice_ = eng
            break
    with open(choice_) as f:
        data = json.load(f)
        k = list(data.keys())
        ch = random.choice(k)
        stop = 1
        while stop:
            stop = 0
            try:
                if choice_ == eng:
                    try:
                        s = random.randint(0,len(data) - 1)
                        str1 = k[s] + '\n' + data[k[s]]['中释'].strip(' ') + '\n' + data[k[s]]['英释'].strip(' ')
                    except KeyError:
                        str1 = k[s] + '\n' + list(data[k[s]].values())[0]
                else:
                    try:
                        str1 = ch + '\n' + data[ch]
                    except KeyError:
                        stop = 1

            except IndexError:
                stop = 1
        try:
            await poke.finish(str1)
        except OneBotAdapterException:
            logger.exception("发送失败！")

@change_language.handle()
async def ch_(event : Event, msg: Message = CommandArg()):
    msg = msg.extract_plain_text().strip()
    if msg not in ('日语','日本語','英语','english'):
        await change_language.finish('请选择正确的语言!')
        # await change_language.finish(msg)
    user = str(event.get_user_id())
    data = get_data()
    found = False
    for uid,choose in data:
        if user == str(uid):
            found = True
            break
    if msg == '日语' or msg == '日本語':
        if found:
            update_data(user,'日语')
            await change_language.finish('更新成功！')
        else:
            add_data(user,'日语')
            await change_language.finish('添加成功！')
    elif msg == '英语' or msg.lower() == 'english':
        if found:
            update_data(user,'英语')
            await change_language.finish('更新成功！')
        else:
            add_data(user,'英语')
            await change_language.finish('添加成功！')

@debug1.handle()
async def d():
    data = get_data()
    a = []
    for uid,choose in data:
        a.append(str(uid))
        a.append(choose)
        a.append('\n')
    await change_language.finish(''.join(a))