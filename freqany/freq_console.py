#!/usr/bin/python3.7.2
# -*- coding: utf-8 -*-
# @Time   : 2019/3/25 22:51
# @Author : william
# @Desc : ==============================================
# 控制台入口
# 通过控制台绑定参数，控制当前程序整体流程
# ======================================================
# @Project : yclass_dictionary
# @FileName: freq_console.py
# @web: http://www.yuketang.net
from freqany import scan_files
from freqany import ana_freq
from freqany import dbutil
import click


@click.command()
@click.option('--username', default='root', help='the database username')
@click.option('--password', prompt='please input password', help='the database password')
@click.option('--table_name', prompt='please input table\'s name', help='the table name')
@click.option('--directory', prompt='please input directory path', help='the directory path')
def console(username, password, table_name, directory):
    """
    字典生成器入口，使用click进行参数的绑定。整体业务流程的整理
    Args:
        username: 连接数据库所使用的用户名
        password: 连接数据库所使用的密码
        table_name: 词频统计需要写入的数据库表名
        directory: 词频分析的文件目录路径，该文件目录中包含所有需要分析的文件

    Returns:
        无返回

    """
    files = scan_files.scan_file(directory)
    print(files)
    word_freq = ana_freq.ana_freq_from_files(files)
    dbutil.connection_db(username=username, password=password)
    dbutil.create_tables(table_name)
    dbutil.insert_word_freq(table_name, word_freq)


if __name__ == '__main__':
    console()
