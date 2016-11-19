# -*- coding: utf-8 -*-
"""
author:Zhong Peng
createDate:2015-12-03
根据author_year_list.csv文件提取每名学者的生涯起始年份和结束年份存入文件
第一列为作者名，第二列为生涯起始年份，第三列为生涯结束年份
"""
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

final_li = []
with open(r'.\author_year_list.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, dialect='excel')
    for row in reader:
        tmp_li = []
        author = row[0]
        year_list = row[1][1:-1].split(", ")
        year_list.sort(key=lambda x: int(x))
        tmp_li.append(author)
        tmp_li.append(year_list[0])
        tmp_li.append(year_list[-1])
        final_li.append(tmp_li)

with open(r'.\author_start_end_year.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, dialect='excel')
    writer.writerows(final_li)
