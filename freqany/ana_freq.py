#!/usr/bin/python3.7.2
# -*- coding: utf-8 -*-
# @Time   : 2019/3/25 22:53
# @Author : william
# @Desc : ==============================================
# 词频分析
# 针对文件列表中的文件，进行集中式的词频分析
# TODO 单词变形的词频如何统计
# ======================================================
# @Project : yclass_dictionary
# @FileName: ana_freq.py
# @web: http://www.yuketang.net
from collections import Counter
import re


def contains_chinese(ustr):
    """
    将字符串中的中文去除
    Args:
        ustr: 字符串

    Returns: 去除中文的字符串

    """
    return any('\u4e00' <= char <= '\u9fff' for char in ustr)


def strip_symbol(ustr):
    """
    将字符串中的标点符号去除
    Args:
        ustr: 带去除字符串

    Returns: 去除标点符号之后的字符串

    """
    return re.sub('[’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+', ' ', ustr)


def ana_freq(file):
    """
    统计单个TXT文件的词频
    Args:
        file: 统计TXT文件

    Returns:
        词频字典 {"单词":"词频"}

    """
    word_counter = Counter()
    with open(file, "rt", encoding="utf-8") as doc:
        for line in doc:
            if contains_chinese(line):
                continue
            line = strip_symbol(line)
            line = line.lower()
            word_counter.update([word for word in re.split('\s+', line) if word != ''])
    return dict(word_counter)


def ana_freq_from_files(files):
    """
    统计多个TXT文件的词频
    Args:
        files: 文件列表

    Returns:
        多个TXT文件的统计词频 {"单词":"词频"}

    """
    freq = Counter()
    for file in files:
        freq = Counter(freq) + Counter(ana_freq(file))
    return dict(freq)
