import MySQLdb

conn = MySQLdb.connect(
    host="121.41.8.92",
    user="*******12",
    passwd="********12",
    db="youyudic",
    port=3306)

cur = conn.cursor()
tables = cur.execute("select * from stardict_mini")
print(cur.fetchall())