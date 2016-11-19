# -*- coding:utf-8 -*-
import sys
sys.path.append('..')
from hits import Graphhits
import paper_author_graph

author_paper_file_path = r'new_paper_author.csv'
citation_file_path = r'..\papergraph\new_aps_citations-2013.csv'
# save_file_path = r'hits_value.csv'
G = paper_author_graph.author_paper_graph(author_paper_file_path)

# 以下两行代码为调用错误函数
# hits_value_dic = Graphhits.hits(G)
# Graphhits.save_hits_value(hits_value_dic, save_file_path)

# 调用hits算法，authority和hub值通过pagerankvalue.csv初始化
hits_value_tuple = Graphhits.paper_author_hits(G)