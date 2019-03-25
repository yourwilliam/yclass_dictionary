#!/usr/bin/python3.7.2
# -*- coding: utf-8 -*-
# @Time   : 2019/3/25 10:37
# @Author : william
# @Desc : ==============================================
# 数据库工具
# 整理数据库相关功能，数据库读、写查询功能
# 通过connection_db连接数据库
# ======================================================
# @Project : yclass_dictionary
# @FileName: console.py
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


# 批量插入executemany
def insert_by_many(dics):
    """
    将dics中的内容批量的写入数据库中
    Args:
        dics: 字典类型，需要写入数据库的相关内容

    Returns:

    """
    param = []
    for word_key, word_value in dics.items():
        param.append([word_value.get("word_name"), str(word_value.get("exchanges")),
                      str(word_value.get("symbols")[0].get("parts"))])
    try:
        sql = 'INSERT INTO dictest values(%s,%s,%s)'
        # 批量插入
        cur.executemany(sql, param)
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()
    print('[insert_by_many executemany] total:')
