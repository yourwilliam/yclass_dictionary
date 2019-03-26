#!/usr/bin/python3.7.2
# -*- coding: utf-8 -*-
# @Time   : 2019/3/26 11:33
# @Author : william
# @Desc : ==============================================
# 从数据库获取字典，导入到anki进行使用
# TODO 新建单词模式，不使用TXT模式，使用apkg模式
# TODO 整理可以从有道词典（Kindle）导出生词本到ANKI进行背诵
# ======================================================
# @Project : yclass_dictionary
# @FileName: anki_console.py
# @web: http://www.yuketang.net
from ankigen import dbutil
from ankigen import ankiexport
import click


@click.command()
@click.option('--username', default='root', help='the database username')
@click.option('--password', prompt='please input password', help='the database password')
@click.option('--table_name', prompt='please input table\'s name', help='the table name')
@click.option('--filepath', prompt='please input filepath', help='the excel dictionary path')
def console(username, password, table_name, filepath):
    """
    anki生成器的入口，通过从数据库获取相应的字典字段，生成ANKI导入txt文档
    Args:
        username: 连接数据库所使用的用户名
        password: 连接数据库所使用的密码
        table_name: 读取字典的数据库名
        filepath: 保存anki导入文件的文件路径

    Returns:
        无返回

    """
    dbutil.connection_db(username, password)
    words = dbutil.select_words(table_name)
    ankiexport.export_anki(filepath, words)


if __name__ == '__main__':
    console()




