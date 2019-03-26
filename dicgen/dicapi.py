#!/usr/bin/python3.7.2
# -*- coding: utf-8 -*-
# @Time   : 2019/3/25 10:37
# @Author : william
# @Desc : ==============================================
# api接口
# 通过API接口访问第三方辞典接口，获取辞典数据
# 已绑定金山词霸接口
# ======================================================
# @Project : yclass_dictionary
# @FileName: freq_console.py
# @web: http://www.yuketang.net
import requests
import time


def get_words_from_api(words):
    """
    将单词的列表，批量的获取第三方接口信息，绑定成为需要写入数据库的字典结构
    Args:
        words: 单词列表

    Returns:
        生成需要写入数据库的字典类型
    """
    dict = {}
    for word in words:
        if type(word) == list:
            wordparam = get_dic_api(word[0])
            dict[word[0]] = wordparam
            time.sleep(2)
        elif type(word) == str:
            wordparam = get_dic_api(word)
            dict[word] = wordparam
            time.sleep(2)
        else:
            print("type error： " + str(type(word)))
    return dict

def get_dic_api(word):
    """
    单个单词通过调用词霸API来获取词霸的单词数据
    Args:
        word: String，单词

    Returns:
        dictionary， 词霸上单词的解释字典

    """
    url = f"http://www.iciba.com/index.php?a=getWordMean&c=search&list=1%2C2%2C3%2C4%2C5%2C8%2C9%2C10%2C12%2C13%2C14%2C18%2C21%2C22%2C3003%2C3005&word={word}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

    req = requests.get(url, headers=headers)
    # 将response转换成为字典格式
    dics = req.json()
    # TODO 判断如果errno为0和不为0 的情况
    return dics.get("baesInfo", None)

# print(get_dic_api("sincere"))