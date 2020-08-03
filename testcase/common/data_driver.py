#!/usr/bin/python
# -*- coding: utf-8 -*-
import os


def get_data_file(file_name):

    return os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'testData','data','test_api.json')


def get_test_data(file_path):

    with open(file_path, 'r') as f:
        content = f.read()

    return content


#if __name__ == '__main__':
#   print("路径：")
#   print(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'testData','data','test_api.json'))
#   print(get_test_data(get_data_file("test_api.json")))
#    pass

