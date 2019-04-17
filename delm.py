#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 4/17/2019 8:59 PM
# @Author  : MUXINGYU


import os
import hashlib
import pandas as pd


def get_file_size(file_name_path):
    # 获取文件的大小,结果保留两位小数，单位为MB
    f_size = os.path.getsize(file_name_path)
    f_size = f_size / float(1024 * 1024)
    return round(f_size, 2)


def get_file_md5(filename):
    if not os.path.isfile(filename):
        return
    my_hash = hashlib.md5()
    f = open(filename, 'rb')
    while True:
        b = f.read(8096)
        if not b:
            break
        my_hash.update(b)
    f.close()
    return my_hash.hexdigest()


def check_all_files(check_path):
    list_files = []
    # 列出文件夹下所有的目录与文件
    cur_list = os.listdir(check_path)
    for i in range(0, len(cur_list)):
        file_path = os.path.join(check_path, cur_list[i])
        if os.path.isdir(file_path):
            list_files.extend(check_all_files(file_path))
        if os.path.isfile(file_path):
            list_files.append([cur_list[i], file_path, get_file_size(file_path), get_file_md5(file_path)])
    return list_files


dir_str = u'E:\电影'.encode('gbk')

a_list = check_all_files(dir_str)
for i in range(len(a_list)):
    a_list[i][0] = a_list[i][0].decode('gbk')
    a_list[i][1] = a_list[i][1].decode('gbk')
mydf = pd.DataFrame(a_list, columns=['file', 'path', 'size(MB)', 'md5'])
mydf.to_excel(r"file_list.xlsx", sheet_name="list")
