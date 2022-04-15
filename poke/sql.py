import sqlite3
_reponame = "pokelanguage.sqlite3"
_sheet = 'pokelanguage'

def init():
    conn = sqlite3.connect(_reponame)
    cursor = conn.cursor()
    sql = f"""create table if not exists {_sheet}(
        uid varchar primary key not null,
        choose varchar not null
    )
    """
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()

def get_data():
    init()
    conn = sqlite3.connect(_reponame)
    cursor = conn.cursor()
    sql = f"""select * from {_sheet}"""
    cursor.execute(sql)
    conn.commit()
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data

def add_data(uid,choose):
    init()
    conn = sqlite3.connect(_reponame)
    cursor = conn.cursor()
    sql = f"""insert into {_sheet} values(?, ?)"""
    cursor.execute(sql, (uid,choose))
    conn.commit()
    cursor.close()
    conn.close()

def update_data(uid,choose):
    init()
    conn = sqlite3.connect(_reponame)
    cursor = conn.cursor()
    sql = f"""update {_sheet} set choose = "{choose}" where uid = "{uid}" """
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()