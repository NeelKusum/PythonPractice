import sqlite3
import re

conn=sqlite3.connect('C:/Users/neelk/AppData/Local/Google/Chrome/User Data/Default/History')
c=conn.cursor()



#x=str(input("Enter the keyword : "))
id=0

result=True

while result:
    result=False
    ids=[]
    for rows in c.execute("SELECT id,url FROM urls Where url LIKE '%gmail%'"):
        print(rows)
        id=rows[0]
        ids.append((id,))
    c.executemany('DELETE from urls WHERE id=?',ids)
    conn.commit()

conn.close()
