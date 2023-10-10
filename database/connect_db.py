import pymysql

def connect(host:str, port:int, user:str, password: str):
    host=host, port=port, user=user, password=password
    conn = pymysql.connect(host=host, port=port, user=user, password=password)
    conn.select_db(database)
    return 