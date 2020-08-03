#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Time    : 2019-07-25 18:37
@Author  : Jian
@Contact : jian.li@shopee.com
@Site    : 
@File    : data_driver.py
@Desc    : Description
"""
import os


def get_data_file(file_name):

    return os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data',file_name)


def get_test_data(file_path):

    with open(file_path, 'r') as f:
        content = f.read()

    return content


if __name__ == '__main__':
   print(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data','test_api.json'))
   print(get_test_data(get_data_file("test_api.json")))
#    pass

