# -*- coding:utf-8 -*-
"""
@author:Zhong Peng
@createDate:2015-11-08
@version:1.0.0
"""
import networkx as nx
import csv
import math


def paper_journal_hits(graph, max_iterations=20, delta=0.0001):
    print "Function hits start"
    nodes = graph.nodes()
    graph_size = len(nodes)
    if graph_size == 0:
        print "Empty graph. There're no nodes."
        return {}
    authority_dic = dict.fromkeys(nodes, 1.0)
    hub_dic = dict.fromkeys(nodes, 1.0)

    with open(r'..\pagerankvalue.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            authority_dic[row[0]] = float(row[1])
            hub_dic[row[0]] = float(row[1])

    for time in range(1, max_iterations + 1):
        norm = 0.0
        for node in nodes:
            authority_dic[node] = 0.0
            for neigh in graph.neighbors(node):
                authority_dic[node] += hub_dic[neigh]
            # norm += authority_dic[node] * authority_dic[node]
            norm += authority_dic[node]
        # norm = math.sqrt(norm)
        print "authority norm:{}".format(norm)
        for node in nodes:
            authority_dic[node] = 1.0 * authority_dic[node] / norm
        with open(r'.\authority\authority%s.csv' % time, 'wb') as csvfile:
            writer = csv.writer(csvfile)
            item_li = sorted(authority_dic.iteritems(), key=lambda x: x[1], reverse=True)
            writer.writerows(item_li)

        norm = 0.0
        for node in nodes:
            hub_dic[node] = 0.0
            for nei in graph.neighbors(node):
                hub_dic[node] += authority_dic[nei]
            # norm += hub_dic[node] * hub_dic[node]
            norm += hub_dic[node]
        # norm = math.sqrt(norm)
        print "hub norm:{}".format(norm)
        for node in nodes:
            hub_dic[node] = hub_dic[node] / norm
        with open(r'.\hub\hub%s.csv' % time, 'wb') as csvfile:
            writer = csv.writer(csvfile)
            item_li = sorted(hub_dic.iteritems(), key=lambda x: x[1], reverse=True)
            writer.writerows(item_li)

        print "Iteration time : {}".format(time)
    return authority_dic, hub_dic


def paper_author_hits(graph, max_iterations=20, delta=0.0001):
    print "Function hits start"
    print "paper autority and hub value inited by pagerankvalue.csv"
    nodes = graph.nodes()
    graph_size = len(nodes)
    if graph_size == 0:
        print "Empty graph. There're no nodes."
        return {}

    authority_dic = {}
    hub_dic = {}
    with open(r'..\papergraph\pagerankvalue.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            authority_dic[row[0]] = eval(row[1])
            hub_dic[row[0]] = eval(row[1])
    jump_count = 0
    for node in nodes:
        if authority_dic.has_key(node):
            jump_count += 1
            print 'jump_count:', jump_count
            continue
        else:
            authority_dic[node] = 1.0
            hub_dic[node] = 1.0

    for time in range(1, max_iterations + 1):
        norm = 0.0
        for node in nodes:
            authority_dic[node] = 0.0
            for neigh in graph.neighbors(node):
                authority_dic[node] += hub_dic[neigh]
            # norm += authority_dic[node] * authority_dic[node]
            norm += authority_dic[node]
        # norm = math.sqrt(norm)
        print "authority norm:{}".format(norm)
        for node in nodes:
            authority_dic[node] = authority_dic[node] / norm
        with open(r'.\authority\authority%s.csv' % time, 'wb') as csvfile:
            writer = csv.writer(csvfile)
            item_li = sorted(authority_dic.iteritems(), key=lambda x: x[1], reverse=True)
            writer.writerows(item_li)

        norm = 0.0
        for node in nodes:
            hub_dic[node] = 0.0
            for nei in graph.neighbors(node):
                hub_dic[node] += authority_dic[nei]
            # norm += hub_dic[node] * hub_dic[node]
            norm += hub_dic[node]
        # norm = math.sqrt(norm)
        print "hub norm:{}".format(norm)
        for node in nodes:
            hub_dic[node] = hub_dic[node] / norm
        with open(r'.\hub\hub%s.csv' % time, 'wb') as csvfile:
            writer = csv.writer(csvfile)
            item_li = sorted(hub_dic.iteritems(), key = lambda x : x[1], reverse = True)
            writer.writerows(item_li)

        print "Iteration time : {}".format(time)
    return authority_dic, hub_dic


def save_hits_value(hits_value, save_file_path):
    print "Function save_hits_value start"
    final_li = []
    for item in hits_value.iteritems():
        tmp_li =[]
        tmp_li.append(item[0])
        tmp_li.append(item[1][0])
        tmp_li.append(item[1][1])
        final_li.append(tmp_li)
    with open(save_file_path, 'wb') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(final_li)
    print "Function save_hits_value over, file save at %s" % save_file_path

if __name__ == '__main__':
    import sys
    sys.path.append('..')
    from paperauthorgraph import paper_author_graph
    author_paper_file_path = r'..\paperauthorgraph\new_paper_author.csv'
    save_file_path = r'.\hits_value.csv'
    G = paper_author_garph.author_paper_graph(author_paper_file_path)
    hits_value = hits(G)
    save_hits_value(hits_value, save_file_path)
