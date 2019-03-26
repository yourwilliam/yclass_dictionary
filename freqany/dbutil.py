#!/usr/bin/python3.7.2
# -*- coding: utf-8 -*-
# @Time   : 2019/3/25 22:53
# @Author : william
# @Desc : ==============================================
# 有鱼英语项目                                         
# 1. 从主库中取出相应的外键字段
# 2. 将词频写入数据库，写入的时候需要指定数据库表名，如果数据库表不存在，则创建数据库表。如果存在则清空数据库表。
# TODO 从主辞典中找到单词的外键，连接到当前词频分析表
# ======================================================
# @Project : yclass_dictionary
# @FileName: dbutil.py
# @web: http://www.yuketang.net
import MySQLdb

conn = None
cur = None


# TODO 使用单子模式构建数据库连接
# TODO 数据库连接关闭
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


def create_tables(table_name):
    """
    判断数据库表是否存在，如果存在，则清空该表，然后添加。
    如果不存在，则创建表。
    Args:
        table_name: 数据库表名

    Returns: 无返回

    """
    cur.execute(f"DROP TABLE IF EXISTS {table_name}")
    sql = f"CREATE TABLE {table_name} (word  CHAR(255) NOT NULL,freq  INT )"
    cur.execute(sql)

# TODO 插入词频的时候增加字段，第三个字段记录为从主字典中查询的单词id写入当前字段中。
def insert_word_freq(table_name, dics):
    """
    将词频字典批量插入数据库
    Args:
        table_name: 数据库表名
        dics: 词频字典值 {"单词","词频"}

    Returns: 无

    """
    param = [[word, word_freq] for word, word_freq in dics.items()]
    try:
        sql = f"INSERT INTO {table_name} values(%s,%s)"
        # 批量插入
        cur.executemany(sql, param)
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()
    print('[insert_by_many executemany] total:')
