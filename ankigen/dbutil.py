#!/usr/bin/python3.7.2
# -*- coding: utf-8 -*-
# @Time   : 2019/3/26 11:34
# @Author : william
# @Desc : ==============================================
# 数据库工具
# TODO 根据词频查询高频单词导入ANKI
# ======================================================
# @Project : yclass_dictionary
# @FileName: dbutil.py
# @web: http://www.yuketang.net
import MySQLdb

conn = None
cur = None


# TODO 使用单子模式构建数据库连接

# 连接数据库
def connection_db(username, password, host="121.41.8.92", port=3306, db="youyudic"):
    """
    绑定数据库连接，所有访问数据库请求需要先调用一次数据库连接来绑定
    将连接直接写为全局变量
    Args:
        username: 必选，数据库的访问用户名，数据库连接时需要提供
        password: 必选，数据库访问密码，数据库连接时需要提供
        host: 数据库主机名，数据库连接的时候需要提供
        port: 数据库连接端口，默认使用3306，如果修改需要提供
        db: 连接数据库名，默认使用youyudic，修改时需要提供

    Returns:

    """
    global conn, cur
    conn = MySQLdb.connect(
        host=host,
        user=username,
        passwd=password,
        db=db,
        port=port,
        use_unicode=True,
        charset="utf8")

    cur = conn.cursor()


def select_words(table_name):
    """
    从指定的字典表中获取字典数据
    Args:
        table_name: 字典数据库的表名

    Returns:
        list类型的数据库信息

    """
    sql = f"select * from {table_name}"
    words = []
    try:
        cur.execute(sql)
        results = cur.fetchall()
        words = [[row[0], row[2]] for row in results]
    except Exception as e:
        print(e)
        print("Error: unable to fecth data")
    return words
