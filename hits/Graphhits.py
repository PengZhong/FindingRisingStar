# -*- coding:utf-8 -*-
'''
@author:Zhong Peng
@createDate:2015-11-08
@version:1.0.0
'''
import networkx as nx
import csv
import math

def hits(graph, max_iterations = 20, delta = 0.0001):
    print "Function hits start"
    nodes = graph.nodes()
    graph_size = len(nodes)
    if graph_size == 0:
        print "Empty graph. There're no nodes."
        return {}
    authority_dic = dict.fromkeys(nodes, 1.0)
    hub_dic = dict.fromkeys(nodes, 1.0)

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
            item_li = sorted(authority_dic.iteritems(), key = lambda x : x[1], reverse = True)
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

def paper_author_hits(graph, max_iterations = 20, delta = 0.0001):
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
            item_li = sorted(authority_dic.iteritems(), key = lambda x : x[1], reverse = True)
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

def paper_journal_hits(graph, max_iterations = 20, delta = 0.0001):
    print "Function hits start"
    print "paper autority and hub value inited by authority20.csv and hub20.csv"
    nodes = graph.nodes()
    graph_size = len(nodes)
    if graph_size == 0:
        print "Empty graph. There're no nodes."
        return {}
    authority_dic = dict.fromkeys(nodes, 1.0)
    hub_dic = dict.fromkeys(nodes, 1.0)

    with open(r'..\paperauthorgraph\authority\authority20.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            content = row[0]
            if content.startswith('10'):
                if authority_dic.has_key(content):
                    authority_dic[content] = eval(row[1])
                else:
                    print "authority content key error:", content
    with open(r'..\paperauthorgraph\hub\hub20.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            content = row[0]
            if content.startswith('10'):
                if hub_dic.has_key(content):
                    hub_dic[content] = eval(row[1])
                else:
                    print "hub content key error:", content

    with open(r'..\before.csv', 'wb') as csvfile:
        writer= csv.writer(csvfile)
        li = sorted(authority_dic.iteritems(), key = lambda x : x[1], reverse = True)
        writer.writerows(li)
    exit(0)

    # auth_jump_count = 0
    # hub_jump_count = 0
    # for node in nodes:
    #     if authority_dic.has_key(node):
    #         auth_jump_count += 1
    #         print 'authority jump:', auth_jump_count
    #         continue
    #     # if hub_dic.has_key(node):
    #     #     hub_jump_count += 1
    #     #     print 'hub jump:', hub_jump_count
    #     #     continue
    #     else:
    #         authority_dic[node] = 1.0
    #         hub_dic[node] = 1.0

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
            item_li = sorted(authority_dic.iteritems(), key = lambda x : x[1], reverse = True)
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

# There're bugs of "zero divided"
# def hits_second_version(graph, max_iterations = 20, delta = 0.0001):
#     print "Function hits start"
#     nodes = graph.nodes()
#     graph_size = len(nodes)
#     if graph_size == 0:
#         print "Empty graph. There're no nodes."
#         return {}
#     hits_value = dict.fromkeys(nodes, [1, 1]) #init authority and hub value

#     for time in range(1, max_iterations + 1):
#         norm = 0

#         # update all authority value(line24-line31)
#         print "Update authority values in the time %s " % time
#         for node in nodes:
#             hits_value[node][0] = 0
#             for incomingNode in graph.neighbors(node):
#                 hits_value[node][0] += hits_value[incomingNode][1]
#             norm += pow(hits_value[node][0], 2)
#         norm = math.sqrt(norm)  # calculate the sum of the squared auth values to normalize
#         for node in nodes:  # update the auth value
#             hits_value[node][0] = hits_value[node][0] / norm

#         # update all hub value(line34-line42)
#         print "Update hub values in the time %s " % time
#         norm = 0
#         for node in nodes:
#             hits_value[node][1] = 0
#             for outgoingNode in graph.neighbors(node):
#                 hits_value[node][1] += hits_value[outgoingNode][0]
#             norm += pow(hits_value[outgoingNode][1], 2)
#         norm = math.sqrt(norm)  # calculate the sum of the squared hub values to normalize
#         for node in nodes:  #update the hub value
#             hits_value[node][1] = hits_value[node][1] / norm

#         print "Iteration time %s over" % time

#     print "Function hits end"
#     return hits_value

# there're some errors in following function
# def hits_first_version(graph, max_iterations = 20, delta = 0.0001):
#     print "Function hits start"
#     nodes = graph.nodes()
#     graph_size = len(nodes)
#     if graph_size == 0:
#         print "Empty graph. There're no nodes."
#         return {}
#     #init authority and hub value {node:[authority, hub]}
#     hits_value = dict.fromkeys(nodes, [1, 1])

#     total_authority = graph_size
#     total_hub = graph_size

#     for time in range(1, max_iterations + 1):
#         diff_authority = 0.0
#         diff_hub = 0.0
#         for node in nodes:
#             value = hits_value[node]
#             authority = 0.0
#             hub = 0.0
#             print node
#             for neighbor in graph.neighbors(node):
#                 authority += hits_value[neighbor][0]
#                 hub += hits_value[neighbor][1]
#             total_authority = total_authority - value[0] + authority
#             total_hub = total_hub - value[1] + hub
#             authority = authority / total_authority
#             hub = hub / total_hub
#             diff_authority += abs(authority - value[0])
#             diff_hub += abs(hub - value[1])
#             hits_value[node][0] = authority
#             hits_value[node][1] = hub
#         print "Iteration times:%s" % time
#         if (diff_authority + diff_hub) < delta:
#             break
#     print "Function hits over"
#     return hits_value

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
