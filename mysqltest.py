import MySQLdb

conn = MySQLdb.connect(
    host="121.41.8.92",
    user="*******123456666",
    passwd="********123456666dgdgg",
    db="youyudic",
    port=3306)

cur = conn.cursor()
tables = cur.execute("select * from stardict_mini")
print(cur.fetchall())