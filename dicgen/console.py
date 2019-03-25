#!/usr/bin/python3.7.2
# -*- coding: utf-8 -*-
# @Time   : 2019/3/25 10:37
# @Author : william
# @Desc : ==============================================
# 程序控制台入口
# 通过控制台参数绑定程序流程参数，控制程序整体流程
# 控制台集成click进行参数绑定，结合excel工具、API工具和数据库工具管理整体流程
# ======================================================
# @Project : yclass_dictionary
# @FileName: console.py
# @web: http://www.yuketang.net
from dicgen import dicapi
from dicgen import excelimport
from dicgen import dbutil
import click


@click.command()
@click.option('--username', default='root', help='the database username')
@click.option('--password', prompt='please input password', help='the database password')
@click.option('--filepath', prompt='please input filepath', help='the excel dictionary path')
def console(username, password, filepath):
    """
    字典生成器入口，使用click进行参数的绑定。整体业务流程的整理
    Args:
        username: 连接数据库所使用的用户名
        password: 连接数据库所使用的密码
        filepath: 解析excel文件的文件路径

    Returns:
        无返回

    """
    # 1. 使用pandas读取excel文件
    word_list = excelimport.readfile(filepath)

    # TODO 为了不重复的去第三方读API，最好在查第三方接口的时候查询一次数据库，过滤掉已经有的词
    # 2. 使用第三方API获取单词列表的所有返回API内容
    word_dicts = dicapi.get_words_from_api(word_list)

    # 3. 连接数据库并将所有单词内容写入数据库
    dbutil.connection_db(username, password)
    dbutil.insert_by_many(word_dicts)


if __name__ == '__main__':
    console()
