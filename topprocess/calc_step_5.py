# -*- coding: utf-8 -*-
"""
author: Zhong Peng
createDate: 2016-01-04
score = (1-d) / n + d * (formular * citation) / 所有作者的（formular * citation）的和
其中formular来自formular_value_range3.csv, citation来自citation3.csv
该文件为计算score值的第一步，计算每名作者的(formular*citation)值，并存入文件
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


for i in [5,]:
    formular_value_path = r'.\formular_value_range_%s.csv' % i
    citation_path = r'.\citation and entropy\citation%s.csv' % i
    formular_dic = formular_value(formular_value_path)
    citation_dic = citation_count(citation_path)
    score_dic = dict()
    for key in formular_dic.keys():
        print key
        score_dic[key] = formular_dic[key] * citation_dic[key]
    with open(r'.\temp\calc_step_5.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(score_dic.iteritems())

final_dic = dict()
total_score = 0
for value in score_dic.itervalues():
    total_score += value

for au in score_dic.iterkeys():
    final_score = 0.2 / 739.0 + 0.8 * score_dic[au] / total_score
    final_dic[au] = final_score

with open(r'.\temp\final_score.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(final_dic.iteritems())
