# -*- coding:utf-8 -*-
import csv
import networkx as nx

def get_journal_by_doi(doi):
    # path_dic = {"PhysRev":"PR", "PhysRevA":"PRA", "PhysRevB":"PRB", "PhysRevC":"PRC", \
    #     "PhysRevD":"PRD", "PhysRevE":"PRE", "PhysRevSeriesI":"PRI", "PhysRevLett":"PRL", \
    #     "PhysRevSTAB":"PRSTAB", "PhysRevSTPER":"PRSTPER", "PhysRevX":"PRX", "RevModPhys":"RMP"}
    tmp = doi.split('/')[1]
    journal = tmp.split('.')[0]
    return journal

def create_paper_journal_graph(file_path):
    print "Function create_paper_journal_graph start"
    journal_li = ["PhysRev", "PhysRevA", "PhysRevB", "PhysRevC", "PhysRevD", "PhysRevE", \
        "PhysRevSeriesI", "PhysRevLett", "PhysRevSTAB", "PhysRevSTPER", "PhysRevX", "RevModPhys"]
    G = nx.Graph()
    with open(file_path, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            doi = row[0]
            journal = get_journal_by_doi(doi)
            if not(journal in journal_li):
                print journal
            else:
                G.add_edge(doi, journal)
    print "Number of Nodes:", G.number_of_nodes()
    print "Number of Edges:", G.number_of_edges()
    print "Function create_paper_journal_graph end"
    if G.has_node('PhysRev'):
        print "PhysRev"
    if G.has_node('PhysRevA'):
        print "PhysRevA"
    if G.has_node('PhysRevB'):
        print "PhysRevB"
    if G.has_node('PhysRevC'):
        print "PhysRevC"
    if G.has_node('PhysRevD'):
        print "PhysRevD"
    if G.has_node('PhysRevE'):
        print "PhysRevE"
    if G.has_node('PhysRevSeriesI'):
        print 'PhysRevSeriesI'
    if G.has_node('PhysRevLett'):
        print 'PhysRevLett'
    if G.has_node('PhysRevSTAB'):
        print 'PhysRevSTAB'
    if G.has_node('PhysRevSTPER'):
        print 'PhysRevSTPER'
    if G.has_node('PhysRevX'):
        print 'PhysRevX'
    if G.has_node('RevModPhys'):
        print 'RevModPhys'
    return G

if __name__ == '__main__':
    # file_path = r'..\paperauthorgraph\new_paper_author.csv'
    # G = create_paper_journal_graph(file_path)
    # print G.number_of_nodes()
    # print G.number_of_edges()
    doi = '10.1103/PhysRevC.74.064906'
    print get_journal_by_doi(doi)

