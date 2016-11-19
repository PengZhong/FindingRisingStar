# -*- coding:utf-8 -*-
'''
@author:Zhong Peng
@createDate:2015-11-05
@lastModified:2015-11-05
@version:1.0.0
create graph by the data from APS dataset, regard journal name, doi, author name as node,
and there're edges between journal and doi, author and doi, doi and author.
'''
import os
import json
import networkx as nx

def getAllFilePath(folder_path):
    '''get all json files' path and return a list'''
    final_file_path_list = []
    for root, dirs, files in os.walk(folder_path):
        for f in files:
            final_file_path_list.append(os.path.join(root, f))
    return final_file_path_list

def get_journal_by_doi(doi):
    '''get a paper's journal name by doi'''
    path_dic = {"PhysRev":"PR", "PhysRevA":"PRA", "PhysRevB":"PRB", "PhysRevC":"PRC", \
        "PhysRevD":"PRD", "PhysRevE":"PRE", "PhysRevSeriesI":"PRI", "PhysRevLett":"PRL", \
        "PhysRevSTAB":"PRSTAB", "PhysRevSTPER":"PRSTPER", "PhysRevX":"PRX", "RevModPhys":"RMP"}
    doi = doi.encode('utf-8')
    subdoi = doi[8:]
    li = subdoi.split('.')
    journal = li[0]
    return journal

def CreateGraph(folder_path, journal_li):
    '''create a graph by the data from APS dataset and return a graph'''
    G = nx.Graph()
    for journal in journal_li:
        G.add_node(journal)
    # G.add_node('PRX')    # for test, in version 1.0.0
    file_path_list = getAllFilePath(folder_path)
    for file_path in file_path_list:
        f = open(file_path, 'r')
        data = json.load(f)
        f.close()

        # in case of lacking doi's data
        if data.has_key('id'):
            doi = data['id']
        else:
            continue

        # incase of lacking author's data
        if data.has_key('authors'):
            authors = data['authors']
            if len(authors) == 0:
                continue
            else:
                # add edges from doi to author_name in the loop
                for author in authors:
                    try:
                        author_name = author['name']
                    except KeyError as e:
                        print "There're no name info in %s" % file_path
                        author_name = '{}{}'.format(doi, 'author')
                    G.add_edge(doi, author_name)
        else:
            continue

        # add a edge from doi to journal
        # G.add_edge(doi, 'PRX')    # for test in version 1.0.0
        G.add_edge(doi, get_journal_by_doi(doi))
        
    return G

if __name__ == '__main__':
    # pay attention to the line 38 and line 69, they just for test.
    all_journal_list = ['PR', 'PRA', 'PRB', 'PRC', 'PRD', 'PRE', \
        'PRI', 'PRL', 'PRSTAB', 'PRSTPER', 'PRX', 'RMP']
    journal_list = ['PRX']
    folder_path = r'E:\APS-DATA\aps-dataset-metadata-2013\PRX'
    graph = CreateGraph(folder_path, journal_list)
    print graph.nodes()
    print 'PRX' in graph.nodes()