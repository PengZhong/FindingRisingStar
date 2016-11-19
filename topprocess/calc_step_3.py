# -*- coding: utf-8 -*-
"""
author: Zhong Peng
createDate: 2016-01-03
score = (1-d) / n + d * (formular * entropy * citation) / 所有作者的（formular * entropy * citation）的和
其中formular来自formular_value_range3.csv, citation来自citation3.csv, entropy来自entropy3.csv
该文件为计算score值的第一步，计算每名作者的(formular*entropy*citation)值，并存入文件
"""
import csv


def formular_value(formular_value_path):
    # get positive_value's dictionary, where key is author's name, value is its value→_→
    formular_value_dic = dict()
    with open(formular_value_path, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            formular_value_dic[row[0]] = float(row[1])
    return formular_value_dic


def citation_count(citation_path):
    # get citation value's dictionary, where key is author's name, value is its value.
    citation_count_dic = dict()
    with open(citation_path, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            author = repr(row[0])[1:-1]
            citation_count_dic[author] = float(row[1])
    return citation_count_dic


def entropy_value(entropy_path):
    # get entropy value's dictionary, where key is author's name, value is its value.
    entropy_value_dic = dict()
    with open(entropy_path, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            author = repr(row[0])[1:-1]
            entropy_value_dic[author] = float(row[1])
    return entropy_value_dic


for i in [3, 5, 7, 10]:
    formular_value_path = r'.\formular_value_range_%s.csv' % i
    citation_path = r'.\citation and entropy\citation%s.csv' % i
    entropy_path = r'.\citation and entropy\entropy%s.csv' % i
    formular_dic = formular_value(formular_value_path)
    citation_dic = citation_count(citation_path)
    entropy_dic = entropy_value(entropy_path)
    score_dic = dict()
    for key in entropy_dic.keys():
        print key
        score_dic[key] = formular_dic[key] * citation_dic[key] * entropy_dic[key]
    with open(r'.\%s\calc_step_3.csv' % i, 'wb') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(score_dic.iteritems())
