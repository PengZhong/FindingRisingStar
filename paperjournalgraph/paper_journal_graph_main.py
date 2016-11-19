# -*- coding:utf-8 -*-
import sys
sys.path.append('..')
from hits import Graphhits
import paper_journal_graph

file_path = r'..\paperauthorgraph\new_paper_author.csv'
# save_hits_value_path = r'.\hits_value.csv'
G = paper_journal_graph.create_paper_journal_graph(file_path)

# 以下两行代码为调用错误函数
# hits_value = Graphhits.hits(G)
# Graphhits.save_hits_value(hits_value, save_hits_value_path)

# 调用hits算法，初始值全部设置为1
# hits_value_tuple = Graphhits.hits(G)

# 调用hits算法，初始值继承自authority.csv和hub.csv
hits_value_tuple = Graphhits.paper_journal_hits(G)