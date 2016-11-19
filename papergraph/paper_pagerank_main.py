# -*-coding:utf-8 -*-
import sys
sys.path.append('..')
from pagerank import pagerank
import apspapergraph

new_citation_file_path = r'..\new_aps_citations-2013.csv'
save_rankvalue_path = r'.\pagerankvalue.csv'
G = apspapergraph.paper_graph(new_citation_file_path)
rank = pagerank.pagerank(G)
pagerank.save_pagerank_value(rank, save_rankvalue_path)
