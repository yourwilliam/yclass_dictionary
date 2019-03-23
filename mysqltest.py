import MySQLdb

conn = MySQLdb.connect(
    host="121.41.8.92",
    user="*******baby11",
    passwd="********baby11",
    db="youyudic",
    port=3306)

cur = conn.cursor()
tables = cur.execute("select * from stardict_mini")
print(cur.fetchall())