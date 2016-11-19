# -*- coding: utf-8 -*-
"""
author: Zhong Peng
create date: 2016-01-13
version: 1.0.0
计算公式 (1-a-b-c) + a*entropy/∑entropy + b*citation/∑citation + c*formular/∑formular 
其中a+b+c=1.0，从0开始以0.1步长增加，entropy与citation文件来自citation and entropy文件夹
formular值来源于当前目录下的文件值
"""
import csv
from decimal import *

# range_li = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
author_num = 685
init_value = (1 - 0.85) / author_num
for year in (3, 5, 7, 10):
    print "year:", year
    citation_dic = dict()
    citation_sum = 0
    with open(r'.\citation and entropy\citation%s.csv' % year, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            author = repr(row[0])[1: -1]
            citation = int(row[1])
            citation_dic[author] = citation
            citation_sum += citation
    print "read citation%s over" % year

    entropy_dic = dict()
    entropy_sum = 0.0
    with open(r'.\citation and entropy\entropy%s.csv' % year, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            entropy = float(row[1])
            entropy_dic[row[0]] = entropy
            entropy_sum += entropy
    print "read entropy%s over" % year

    formular_dic = dict()
    formular_sum = 0.0
    with open(r'.\formular_value_range_%s.csv' % year, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            formular_val = float(row[1])
            formular_dic[row[0]] = formular_val
            formular_sum += formular_val
    print "read formular_value_range_%s over" % year

    value_dic = dict()
    for a in range(0, 86, 5):
        for b in range(0, 86-a+1, 5):
            c = 85 - a - b
            coefficient_1 = Decimal('0.01') * a
            coefficient_2 = Decimal('0.01') * b
            coefficient_3 = Decimal('0.01') * c
            print coefficient_1, coefficient_2, coefficient_3
            for key in entropy_dic.keys():
                value_dic[key] = init_value + float(coefficient_1) * entropy_dic[key] / entropy_sum + \
                                 float(coefficient_2) * citation_dic[key] / citation_sum + \
                                 float(coefficient_3) * formular_dic[key] / formular_sum
            
            path = r'.\calc_step_2_result\%s_%s_%s_%s.csv' % (year, coefficient_1, coefficient_2, coefficient_3)
            value_li = sorted(value_dic.items(), key=lambda x: x[1], reverse=True)
            with open(path, 'wb') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(value_li)
            print "file write over"
