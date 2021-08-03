# -*- coding: utf-8 -*-
# @Time    : 2021/7/30 10:45 下午
# @Author  : YanYi
# @File    : data_cleaning.py

"""
    数据清洗

"""
import pandas as pd
import matplotlib.pyplot as plt


#
def data_cleaning():
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

    file_path = r"/Users/yiyan/PycharmProjects/PyChart/File/aaa.csv"
    lc = pd.read_csv(file_path)

    # lc['月份'] = pd.to_datetime(lc['销售时间'])
    print(lc)
    # 修改时间新增月份列
    plt.hist(lc)
    plt.show()


#
if __name__ == '__main__':
    data_cleaning()
