# -*- coding:utf-8 -*-
"""
@author:Zhong Peng
@createDate:2015-12-02
@version:1.0.0
"""
import csv
import sys

top500_citation_author = []
with open(r'.\author_citation_count.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, dialect='excel')
    for row in reader:
        if reader.line_num <= 500:
            top500_citation_author.append(row[0])
        else:
            break
print len(top500_citation_author)

author_pagerank_dic = {}
with open(r'.\pagerank_undirected.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, dialect='excel')
    for row in reader:
        author_pagerank_dic[row[0]] = row[1]

author_pagerank_li = [(author, author_pagerank_dic[author]) for author in top500_citation_author]

with open(r'.\top500_citation_author_pagerank_value.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, dialect='excel')
    writer.writerows(author_pagerank_li)
