import xlrd,sqlite3


# 创建数据库( flora_name.db )并建立(  )
def create_db():
    conn = sqlite3.connect('flora_name.db')
    print("Opened database successfully")
    conn.execute("""CREATE TABLE FLORA_NAME (id INTEGER PRIMARY KEY,CPNI_CODE TEXT,FAMILY_LATIN_NAME TEXT,FAMILY_ZN_NAME TEXT,GENUS_NAME TEXT,GENUS_ZH_NAME TEXT,SPECIFIC_NAME TEXT,LATIN_NAME TEXT,ZH_NAME TEXT,LEVEL TEXT,LITERATURE TEXT);""")
    print("Table created FLORA_NAME successfully")
    conn.close()

# 插入数据
def insert(row_value):
    CPNI_CODE             = row_value[0]
    FAMILY_LATIN_NAME     = row_value[1]
    FAMILY_ZN_NAME        = row_value[2]
    GENUS_NAME            = row_value[3]
    GENUS_ZH_NAME         = row_value[4]
    SPECIFIC_NAME         = row_value[5]
    LATIN_NAME            = row_value[6]
    ZH_NAME               = row_value[7]
    LEVEL                 = row_value[8]
    LITERATURE            = row_value[9]
    params = (CPNI_CODE,FAMILY_LATIN_NAME, FAMILY_ZN_NAME, GENUS_NAME, GENUS_ZH_NAME,SPECIFIC_NAME,LATIN_NAME,ZH_NAME,LEVEL,LITERATURE)
    conn.execute("INSERT INTO FLORA_NAME VALUES (NULL,?,?,?,?,?,?,?,?,?,?)",params)
    conn.commit()
    print("Insert ",row_value ," successfully","\n")

data = xlrd.open_workbook("Chinese_Plant_Names_Index_CPNI.v2.0.xlsx")
table = data.sheets()[0]

create_db()
conn = sqlite3.connect('flora_name.db')

for rownum in range(table.nrows):
    row_value = table.row_values(rownum)
    print(type(row_value))
    insert(row_value)

conn.close()

