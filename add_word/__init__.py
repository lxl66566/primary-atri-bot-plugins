from nonebot import on_command
from nonebot.adapters.onebot.v11 import MessageSegment,MessageEvent,PRIVATE
from nonebot.params import CommandArg, Message
import json

add_word = on_command('wa', priority=1, block=True,permission=PRIVATE)

@add_word.handle()
async def _(event: MessageEvent,msg: Message = CommandArg()):
    if str(event.get_user_id()) != '1421962366':
        await add_word.finish()
    args = list(msg.extract_plain_text().split())
    if len(args) == 0:
        await add_word.finish("请输入单词！")
    eng = ['english: ']
    jap = ['japanese: ']
    with open(r'D:\program\Qt\merge_anki\notebook.json','r',encoding='utf-8') as f:
        notebook = json.load(f)
        notebook['english']['default'] = set(notebook['english']['default'])
        notebook['japanese']['default'] = set(notebook['japanese']['default'])
        for i in args:
            if i.encode().isalpha():
                lan = 'english'
                eng.append(i)
                eng.append(' ')
            else:
                lan = 'japanese'
                jap.append(i)
                jap.append(' ')
            if(i in notebook[lan]['default']):
                continue
            else:
                notebook[lan]['default'].add(i)
    with open(r'D:\program\Qt\wordsreciterGUI\wordsreciter GUI v1.3.1\notebook.json','w',encoding='utf-8') as f:
        notebook['english']['default'] = list(notebook['english']['default'])
        notebook['japanese']['default'] = list(notebook['japanese']['default'])
        json.dump(notebook,f,indent=4,ensure_ascii=False)
        ans = '添加成功'
        if len(eng) != 1:
            ans += '\n' + ''.join(eng)
        if(len(jap)) != 1:
            ans += '\n' + ''.join(jap)
        await add_word.finish(ans)