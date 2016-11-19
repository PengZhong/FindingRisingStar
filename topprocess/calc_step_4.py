# -*- coding: utf-8 -*-
"""
author: Zhong Peng
createDate: 2016-01-04
score = (1-d) / n + d * (formular * entropy * citation) / 所有作者的（formular * entropy * citation）的和
其中formular来自formular_value_range3.csv, citation来自citation3.csv, entropy来自entropy3.csv
该文件为计算score值的第二步，根据第一步生成文件计算最终算式的值
"""
import csv

for i in [3, 5, 7, 10]:
    print "***************************"
    path = r'.\%s\calc_step_3.csv' % i
    print 'path:', path
    author_score_dic = dict()
    with open(path, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        total_score = 0
        author_count = 0
        for row in reader:
            value = float(row[1])
            author_score_dic[row[0]] = value
            total_score += value
            author_count += 1
    print "author_count:", author_count
    print "total_score", total_score
    for d in [elem * 0.1 for elem in range(0, 10)]:
        print d
        final_dic = dict()
        for key in author_score_dic.iterkeys():
            final_score = (1.0 - d) / author_count + d * author_score_dic[key] / total_score
            final_dic[key] = final_score
        with open(r'.\%s\%s.csv' % (i, d), 'wb') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(final_dic.iteritems())
