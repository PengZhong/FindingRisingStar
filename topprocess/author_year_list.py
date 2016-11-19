# -*- coding: utf-8 -*-
"""
author:Zhong Peng
createDate:2015-12-03
根据new_author_paper_list_all.csv生成作者与发表的论文年份对应的文件
第一列为作者名，第二列为作者发表的每篇论文的年份的列表
"""
import csv
import os
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def get_path_by_doi(doi):
    """根据文章doi找到json原数据文件的位置,返回值为json文件的绝对路径"""
    path = r"E:\APS-DATA\aps-dataset-metadata-2013"
    folder_dict = {"PhysRev":"PR", "PhysRevA":"PRA", "PhysRevB":"PRB", "PhysRevC":"PRC", "PhysRevD":"PRD", \
        "PhysRevE":"PRE", "PhysRevSeriesI":"PRI", "PhysRevLett":"PRL", "PhysRevSTAB":"PRSTAB", \
        "PhysRevSTPER":"PRSTPER", "PhysRevX":"PRX", "RevModPhys":"RMP"}
    path_doi = doi[8:]
    filename = '{}{}'.format(path_doi, '.json')
    li = path_doi.split('.')
    path = os.path.join(path, folder_dict[li[0]], li[1], filename)
    return path


def get_year_from_file(path):
    """根据json文件路径查找该篇论文发表的年份"""
    f = open(path, 'r')
    data = json.load(f)
    f.close()
    date = data['date']
    year = date[0:4]
    return int(year)


author_li = []
author_year_dic = {}
with open(r'.\new_author_paper_list.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        author = row[0]
        author_li.append(author)
        doi_year_li = []
        doi_li = row[1][2:-2].split("', '")
        for doi in doi_li:
            path = get_path_by_doi(doi)
            year = get_year_from_file(path)
            doi_year_li.append(year)
        doi_year_li.sort()
        author_year_dic[author] = doi_year_li

final_li = sorted(author_year_dic.iteritems(), key=lambda x: author_li.index(x[0]))

with open(r'.\author_year_list.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(final_li)
