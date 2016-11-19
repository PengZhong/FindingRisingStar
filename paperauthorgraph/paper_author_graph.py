# -*- coding:utf-8 -*-
'''
@author:Zhong Peng
@createDate:2015-11-08
@version:1.0.0
create author paper undirected graph.
'''
import networkx as nx
import csv

def author_paper_graph(author_paper_file_path):
    print 'Function author_paper_graph start'
    G = nx.Graph()
    with open(author_paper_file_path, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        count = 0
        for row in reader:
            G.add_edge(row[0], row[1])
            count += 1
            print count
    print 'Function author_paper_graph end'
    print "number_of_nodes:", G.number_of_nodes()
    print "number_of_edges:", G.number_of_edges()
    return G

if __name__ == '__main__':
    author_paper_file_path = r'new_paper_author.csv'
    G = author_paper_graph(author_paper_file_path)
    print G.number_of_nodes()
    print G.number_of_edges()
