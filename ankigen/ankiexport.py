#!/usr/bin/python3.7.2
# -*- coding: utf-8 -*-
# @Time   : 2019/3/26 11:34
# @Author : william
# @Desc : ==============================================
# ANKi格式文件生成工具
# TODO 做更多适合ANKi使用的工具
# ======================================================
# @Project : yclass_dictionary
# @FileName: ankiexport.py
# @web: http://www.yuketang.net


def export_anki(filepath, words):
    """
    将获取的words导出到anki可以导入的文件中去，中间使用\t制表符进行标识。导入anki的时候，需要使用\t制表符进行分割。
    Args:
        filepath: 到处的文件的文件地址
        words: list形式的单词格式

    Returns:

    """
    with open(filepath, "wt", encoding="utf-8") as anki_file:
        for word in words:
            anki_file.write(word[0] + '\t' + word[1] + '\n')
