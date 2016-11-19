# -*- coding:utf-8 -*-
'''
@author:Zhong Peng
@createDate:2015-11-06
@version:1.0.0
create graph by the data of aps, regard paper as node.
while there is a paper A cited by B, there is a directed edge from B to A.
'''
import networkx as nx
import csv

def paper_graph(citation_file_path):
    '''
    create paper graph that edges' direction represent citing or cited relation.
    for example:if A cited by B, then there's a directed edge from B to A.
    '''
    print "Function paper_graph start"
    G = nx.DiGraph()
    with open(citation_file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            citing_doi = row[0].encode('utf-8')
            cited_doi = row[1].encode('utf-8')
            G.add_edge(citing_doi, cited_doi)
    print "Function paper_graph end"
    return G

if __name__ == '__main__':
    citation_file_path = r'E:\APS-DATA\aps-dataset-citations-2013\aps-dataset-citations-2013.csv'
    G = paper_graph(citation_file_path)
    print G.number_of_nodes()
    print G.number_of_edges()
    print G.number_of_selfloops()
