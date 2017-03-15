import xlrd,sqlite3


# 创建数据库( flora_name.db )并建立(  )
def create_db():
    conn = sqlite3.connect('flora_name.db')
    print("Opened database successfully")
    conn.execute("""CREATE TABLE SYNONYM (id INTEGER PRIMARY KEY,CPNI_CODE TEXT,RECTIFICATION_NAME TEXT,SYNONYM_NAME TEXT,GENERIC_NAME TEXT,SYNONYM_LITERATURE TEXT);""")
    print("Table created FLORA_NAME successfully")
    conn.close()

# 插入数据
def insert(row_value):
    print("Opened database flora_name.db successfully")
    CPNI_CODE           = row_value[0]
    RECTIFICATION_NAME     = row_value[1]
    SYNONYM_NAME        = row_value[2]
    GENERIC_NAME = row_value[3]
    SYNONYM_LITERATURE      = row_value[4]
    params = (CPNI_CODE,RECTIFICATION_NAME, SYNONYM_NAME, GENERIC_NAME, SYNONYM_LITERATURE)
    conn.execute("INSERT INTO SYNONYM VALUES (NULL,?,?,?,?,?)",params)
    conn.commit()
    print("Insert ",row_value ," successfully","\n")

data = xlrd.open_workbook("Chinese_Plant_Names_Index_CPNI.v2.0.xlsx")
table = data.sheets()[1]

create_db()
conn = sqlite3.connect('flora_name.db')

for rownum in range(table.nrows):
    row_value = table.row_values(rownum)
    print(type(row_value))
    insert(row_value)

conn.close()

