from nonebot import on_command
from nonebot.adapters.onebot.v11 import Message,MessageEvent,Bot,GROUP
# from nonebot.typing import T_Handler, T_RuleChecker, T_State
from nonebot.params import CommandArg
from .sql import add_data,update_data,get_data

meal = on_command('带饭',aliases = {'带水','帶飯'},priority=1, block=True,permission=GROUP)

@meal.handle()
async def _(bot:Bot, event: MessageEvent, msg: Message = CommandArg()):
    moneyadd = 10
    users = []
    groupid = '_' + str(event.group_id)
    taker = str(event.get_user_id())
    mode = '0'
    for msg_seg in msg:
        if msg_seg.type == "at":
            users.append(msg_seg.data["qq"])
        elif msg_seg.type == "text":
            for text in str(msg_seg).split():
                try:
                    if moneyadd == 10:
                        moneyadd = float(text)
                    else:
                        await meal.finish('指令有误，请重新输入')
                except ValueError:
                    if mode == '0':
                        mode = text
                    else:
                        await meal.finish('指令有误，请重新输入')
                    
    if mode not in ('all','add','set','info','0'):
        await meal.finish('指令有误，请重新输入')
    if mode == 'all':
        users.clear()
        seikou = False
        for user1,user2,money in get_data(groupid):
            if user2 is user1:
                continue
            if user1 == taker:
                update_data(groupid,user1,user2, money - moneyadd)
                seikou = True
            elif user2 == taker:
                update_data(groupid,user1,user2, money + moneyadd)
                seikou = True
        if seikou:
            await meal.finish('带饭成功')
        else:
            await meal.finish('带饭失败，请先使用add指令')

    elif mode == 'add':
        users.append(taker)
        userbefore = set()
        for user1,user2,money in get_data(groupid):
            userbefore.add(user1)
            userbefore.add(user2)
        for i in users:
            if i in userbefore:
                continue
            for j in userbefore:
                add_data(groupid,j,i,0)
            userbefore.add(i)
        await meal.finish('添加成功')

    elif mode == 'info':
        dict = {}
        for user1,user2,money in get_data(groupid):
            if user1 not in dict:
                temp = await bot.get_group_member_info(group_id=groupid[1:], user_id=user1)
                dict[user1] = temp.get('nickname', '')
            if user2 not in dict:
                temp = await bot.get_group_member_info(group_id=groupid[1:], user_id=user2)
                dict[user2] = temp.get('nickname', '')

        s = ['in group ',groupid[1:],':\n']
        for user1,user2,money in get_data(groupid):
            s.extend([dict[user1],' ',dict[user2],' ',str(money),'\n'])
        if s[-1] == '\n':
            s.pop()
        await meal.finish(''.join(s))
    
    elif mode == 'set':
        if len(users) != 2:
            await meal.finish('输入数据不合法，请重新输入')
        for user1,user2,money in get_data(groupid):
            if user1 == users[0] and user2 == users[1]:
                update_data(groupid,users[0],users[1],moneyadd)
                await meal.finish('修改完成')
            elif user1 == users[1] and user2 == users[0]:
                update_data(groupid,users[1],users[0],moneyadd)
                await meal.finish('修改完成')
        await meal.finish('未找到可修改部分')
    
    elif len(users) != 0:
        for user1,user2,money in get_data(groupid):
            if user2 is user1:
                continue
            if user1 == taker and user2 in users:
                update_data(groupid,user1,user2, money - moneyadd)
            elif user2 == taker and user1 in users:
                update_data(groupid,user1,user2, money + moneyadd)
        await meal.finish('带饭成功')