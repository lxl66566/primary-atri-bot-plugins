import sqlite3
from datetime import datetime
_reponame = 'moneycalc.sqlite'
# _sheet = 'pokelanguage'

def add_into_log(s):
    with open('log_of_moneycalc.txt','a') as f:
        f.write(s + '\n')

def init(_sheet):
    conn = sqlite3.connect(_reponame)
    cursor = conn.cursor()
    sql = f"""create table if not exists {_sheet}(
        user1 varchar not null,
        user2 varchar,
        money real
    )
    """#money正表示user1欠user2钱。为负则反之
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()

def get_data(_sheet):
    init(_sheet)
    conn = sqlite3.connect(_reponame)
    cursor = conn.cursor()
    sql = f"""select * from {_sheet}"""
    cursor.execute(sql)
    conn.commit()
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data

def add_data(_sheet,user1,user2,money):
    init(_sheet)
    conn = sqlite3.connect(_reponame)
    cursor = conn.cursor()
    sql = f"""insert into {_sheet} values({user1}, {user2}, {money})"""
    cursor.execute(sql)
    conn.commit()
    add_into_log(f'add group= {_sheet} user1= {user1} user2= {user2} money= {str(money)} time= {str(datetime.now())}')
    cursor.close()
    conn.close()

def update_data(_sheet,user1,user2,money):
    init(_sheet)
    conn = sqlite3.connect(_reponame)
    cursor = conn.cursor()
    sql = f"""update {_sheet} set money = "{money}" where user1 = "{user1}" and user2 = "{user2}" """
    cursor.execute(sql)
    add_into_log(f'update group={_sheet} user1= {user1} user2= {user2} money= {str(money)} time= {str(datetime.now())}')
    conn.commit()
    cursor.close()
    conn.close()