import xlrd,sqlite3


# 创建数据库( flora_name.db )并建立(  )
def create_db():
    conn = sqlite3.connect('flora_name.db')
    print("Opened database successfully")
    conn.execute("""CREATE TABLE FLORA_ZH_NAME (id INTEGER PRIMARY KEY,CPNI_CODE TEXT,LATIN_NAME TEXT,CN_NAME TEXT,CN_NAME_SOURCE TEXT,NAME_TYPE TEXT);""")
    print("Table created FLORA_NAME successfully")
    conn.close()

# 插入数据
def insert(row_value):
    print("Opened database flora_name.db successfully")
    CPNI_CODE      = row_value[0]
    LATIN_NAME     = row_value[1]
    CN_NAME        = row_value[2]
    CN_NAME_SOURCE = row_value[3]
    NAME_TYPE      = row_value[4]
    params         = (CPNI_CODE,LATIN_NAME, CN_NAME, CN_NAME_SOURCE, NAME_TYPE)
    conn.execute("INSERT INTO FLORA_ZH_NAME VALUES (NULL,?,?,?,?,?)",params)
    conn.commit()
    print("Insert ",row_value ," successfully","\n")

data = xlrd.open_workbook("Chinese_Plant_Names_Index_CPNI.v2.0.xlsx")
table = data.sheets()[2]

create_db()
conn = sqlite3.connect('flora_name.db')

for rownum in range(table.nrows):
    row_value = table.row_values(rownum)
    print(type(row_value))
    insert(row_value)

conn.close()

