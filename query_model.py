import sqlite3

conn = sqlite3.connect("flora_name.db")

cur = conn.cursor()

table_names = cur.execute("select name from sqlite_master where type='table' order by name")
all = table_names.fetchall()
names = {}

def get_table_name(argument):
    switcher = {
        1: ["FLORA_NAME","ZH_NAME"],
        2: ["FLORA_ZH_NAME","CN_NAME"],
        3: ["SYNONYM","RECTIFICATION_NAME"],
    }
    return switcher.get(argument, "nothing")

def initdata():
    for one in all:
        if one[0] == "FLORA_NAME":
            names["FLORA_NAME"] = "1.中国植物物种名录"
        elif one[0] == "FLORA_ZH_NAME":
            names["FLORA_ZH_NAME"] = "2.中国植物物种中文名录"
        elif one[0] == "SYNONYM":
            names["SYNONYM"] = "3.中国植物物种拉丁异名名录"
    print("你想查询哪一个选项?")
    print(names["FLORA_NAME"])
    print(names["FLORA_ZH_NAME"])
    print(names["SYNONYM"])
    floraname = input("请输入一个选项（仅限数字编号）:")
    return floraname

a = initdata()
while int(a) > 0 and int(a) < 4:
    keyword = input("请输入一个植物种类的关键字进行查询:")
    table = get_table_name(int(a))[0]
    col = get_table_name(int(a))[1]
    sql_str = "select * from "+table+" where "+col+" like ? "
    result = cur.execute(sql_str,('%'+keyword+'%',))
    all = result.fetchall()
    if len(all) == 0:
        print("\n没有查到"+keyword+"的数据，请重新选择:\n")
    else:
        for row in all:
            print("%5s || %14s || %80s || %15s || %20s || %10s ||" % (row[0],row[1],row[2],row[3],row[4],row[5]))
    a = initdata()
else:
    print("input value error")
cur.close()