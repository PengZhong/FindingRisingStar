# -*- coding:utf-8 -*-
"""
@author:Zhong Peng
@createDate:2015-11-26
@version:1.0.0
根据new_aps_citation-2013.csv统计出doi对应的被引用次数
"""
import csv
# get cited dois by citation file, save dois in cited_doi.
cited_doi = []
with open(r'..\papergraph\new_aps_citations-2013.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        cited_doi.append(row[1])
print "get cited_doi over"
print len(cited_doi)    # 5957480
s = set(cited_doi)
print len(s)    # 452258
cited_doi_li = []
for doi in s:
    tmp_li = []
    print doi
    tmp_li.append(doi)
    tmp_li.append(cited_doi.count(doi))
    cited_doi_li.append(tmp_li)
print len(cited_doi_li)    # 452258
# cited_doi_tuple_li = [(doi, cited_doi.count(doi)) for doi in s]
# print cited_doi_tuple_li[0]
# print len(cited_doi_tuple_li)
with open(r'.\doi_citation_count.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(cited_doi_li)
