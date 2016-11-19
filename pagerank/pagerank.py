# -*- coding:utf-8 -*-
"""
@author:Zhong Peng
@createDate:2015-11-05
@version:1.0.0
"""
import networkx as nx
import csv


def pagerank_undirected(graph, damping_factor=0.85, max_iterations=20, min_delta=0.0001):
    """page rank algorithm for undirected graph"""
    print """page rank for undirected graph start..."""
    nodes = graph.nodes()
    graph_size = len(nodes)
    if graph_size == 0:
        print "Empty graph. There're no nodes."
        return {}
    rank = dict.fromkeys(nodes, 1.0 / graph_size)
    min_value = (1.0 - damping_factor) / graph_size
    for times in range(1, max_iterations + 1):
        diff = 0.0  # the gap between two iterations
        for node in nodes:
            rankScore = min_value
            for neighbor in graph.neighbors(node):
                rankScore += damping_factor * rank[neighbor] / len(graph.neighbors(neighbor))
            diff += abs(rank[node] - rankScore)
            rank[node] = rankScore
        print "iteration time: %s" % times
        if diff < min_delta:
            break
    print "page rank for undirected graph over"
    return rank


def pagerank(graph, damping_factor=0.85, max_iterations=20, min_delta=0.0001):
    """run pagerank on the directed graph and return a dict which like {"node1":0.1, "node2":0.2...}"""
    print "pagerank algorithm start..."
    nodes = graph.nodes()
    graph_size = len(nodes)
    if graph_size == 0:
        print "Empty graph. There're no nodes."
        return {}
    rank = dict.fromkeys(nodes, 1.0 / graph_size)
    min_value = (1.0 - damping_factor) / graph_size
    for times in range(1, max_iterations + 1):
        diff = 0.0    # the gap between two iterations
        for node in nodes:
            rankScore = min_value
            for pre_node in graph.predecessors(node):
                rankScore += damping_factor * rank[pre_node] / len(graph.successors(pre_node))
            diff += abs(rank[node] - rankScore)
            rank[node] = rankScore
        print "iteration time: %s" % times
        if diff < min_delta:
            break
    # rank_li = sorted(rank.iteritems(), key = lambda x : x[1], reverse = True)
    print "PageRank algorithm over"
    return rank


def save_pagerank_value(rank_dic, file_path):
    """save the pagerank value into files"""
    rank_li = sorted(rank_dic.iteritems(), key=lambda x: x[1], reverse=True)
    with open(file_path, 'wb') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rank_li)
    print "File write over at %s " % file_path

if __name__ == '__main__':
    import sys
    sys.path.append(r'papergraph')
    import apspapergraph
    citation_file_path = r'E:\APS-DATA\aps-dataset-citations-2013\aps-dataset-citations-2013.csv'
    pagerank_dic = pagerank(apsgraph.CreateGraph(citation_file_path))
    print pagerank_dic
