# -*- coding: utf-8 -*-
"""
author: Zhong Peng
createDate: 2015-12-10
根据原有的author_citation_count.csv和author_year_list.csv创建新的作者引用量文件，
其中只包含学术生涯大于20的学者。
"""
import csv

author_start_end_year_dic = {}
with open(r'.\author_start_end_year.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, dialect='excel')
    for row in reader:
        year_li = list()
        year_li.append(int(row[1]))
        year_li.append(int(row[2]))
        author_start_end_year_dic[row[0]] = year_li
print "author_start_end_year_dic over"

author_career_gt20_citation_count_li = list()
with open(r'.\author_citation_count.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        author = row[0]
        year_li = author_start_end_year_dic[author]
        if (year_li[1] - year_li[0]) >= 20:
            author_career_gt20_citation_count_li.append(row)
print "author_citation_count_dic over"

with open(r'.\author_career_gt20_citation_count.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, dialect='excel')
    writer.writerows(author_career_gt20_citation_count_li)
print "write file over"
