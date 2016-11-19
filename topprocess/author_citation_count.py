# -*- coding: utf-8 -*-
"""
@author:Zhong Peng
@createDate:2015-11-27
@version:1.0.0
统计作者对应的被引用次数，并按照从大到小顺序存入csv
"""
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

doi_citation_dic = {}
with open(r'.\doi_citation_count.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        doi_citation_dic[row[0]] = int(row[1])
print 'doi_citation_dict over'

author_citation_dic = {}
zero_citation_paper_li = []
with open(r'.\new_author_paper_list.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    count = 0
    for row in reader:
        count += 1
        print count
        total_citation = 0
        author = row[0]
        doi_list = row[1][2:-2].split("', '")
        for doi in doi_list:
            if doi_citation_dic.has_key(doi):
                total_citation += doi_citation_dic[doi]
            else:
                tmp_li = []
                tmp_li.append(doi)
                zero_citation_paper_li.append(tmp_li)
        author_citation_dic[author] = total_citation
print 'author_citation_count_dict over'

with open(r'.\zero_citation_paper.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)
    for paper in zero_citation_paper_li:
        writer.writerow(paper)

final_li = sorted(author_citation_dic.items(), key=lambda x: x[1], reverse=True)
print 'sort over'

with open(r'.\author_citation_count.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(final_li)
print 'write author_citation_count.csv over'

