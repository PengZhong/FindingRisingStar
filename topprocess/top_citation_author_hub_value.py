# -*- coding:utf-8 -*-
"""
@author:Zhong Peng
@createDate:2015-12-02
@version:1.0.0
"""
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

top500_citation_author = []
with open(r'.\author_citation_count.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, dialect='excel')
    for row in reader:
        if reader.line_num <= 500:
            top500_citation_author.append(row[0])
        else:
            break
print len(top500_citation_author)

author_hub_dic = {}
with open(r'.\hub\hub20.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        author_hub_dic[row[0]] = row[1]

author_hub_li = [(author, author_hub_dic[author]) for author in top500_citation_author]

with open(r'.\top500_citation_author_hub_value.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, dialect='excel')
    writer.writerows(author_hub_li)
