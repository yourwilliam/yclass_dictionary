#!/usr/bin/python3.7.2
# -*- coding: utf-8 -*-
# @Time   : 2019/3/25 10:37
# @Author : william
# @Desc : ==============================================
# excel导入工具
# 导入excel辞典到本地，读取excel数据
# ======================================================
# @Project : yclass_dictionary
# @FileName: freq_console.py
# @web: http://www.yuketang.net
import pandas as pd
import numpy as np


def readfile(filename):
    """
    从excel中读取内容，将字典的内容读取到程序形成词语的列表
    Args:
        filename: String，系统中的文件路径，建议使用绝对路径模式。

    Returns:
        List， 单词的列表

    """
    df = pd.read_excel(filename, sheet_name=3, index_col=1, usecols=[0, 2], nrows=5)
    words_data = np.array(df)
    words = words_data.tolist()
    return words

# print(readfile("D:\\share\\dic.xlsx"))