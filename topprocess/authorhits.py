# -*- coding:utf-8 -*-
"""
@author:Zhong Peng
@createDate:2015-11-26
@version:1.0.0
"""
import csv
import sys
sys.path.append('..')
import networkx as nx
from hits import Graphhits
reload(sys)
sys.setdefaultencoding('utf-8')

paper_author_dic = {}
with open(r'.\new_author_paper_list.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, dialect='excel')
    for row in reader:
        author = row[0]
        paper_li = row[1][2:-2].split("\', \'")
        for doi in paper_li:
            if paper_author_dic.has_key(doi):
                paper_author_dic[doi].append(author)
            else:
                paper_author_dic[doi] = []
                paper_author_dic[doi].append(author)
print 'paper_author_dic initial over'

G = nx.Graph()
for item in paper_author_dic.iteritems():
    author_li = item[1]
    author_num = len(author_li)
    for i in range(0, author_num - 1):
        for j in range(i + 1, author_num):
            G.add_edge(author_li[i], author_li[j])
print "nodes number:", G.number_of_nodes()
print "edges number:", G.number_of_edges()

Graphhits.hits(G)
