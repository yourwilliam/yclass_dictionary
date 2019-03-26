#!/usr/bin/python3.7.2
# -*- coding: utf-8 -*-
# @Time   : 2019/3/25 22:51
# @Author : william
# @Desc : ==============================================
# 索引文件夹
# 查询文件夹中的所有可读文件
# TODO 当前仅支持TXT格式文件，后续增加word格式文件
# TODO 完成word格式文件之后，后续支持解析HTML格式文件
# ======================================================
# @Project : yclass_dictionary
# @FileName: scan_files.py
# @web: http://www.yuketang.net
import os


def scan_file(path):
    """
    查询和返回文件夹中的所有文件的路径
    Args:
        path: 文件夹路径

    Returns:
        文件夹中的所有文件路径列表 List
    """
    files_paths = []
    if os.path.isdir(path):
        files = os.listdir(path)
        for file in files:
            if not os.path.isdir(file):
                files_paths.append(path + "\\" + file)
    else:
        print("please input a dir!")
    print(files_paths)
    return files_paths
