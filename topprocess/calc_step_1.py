# -*- coding: utf-8 -*-
"""
author: Zhong Peng
createDate: 2015-12-06
HITS(author)*∑(author_order_in_paper_i*PR(paper_i)*HITS(journal_i))
"""
import json
import csv
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

base_path = r'F:\PZ\aps-dataset-metadata-2013'
# base_path = r'E:\APS-DATA\aps-dataset-metadata-2013'
start_year = 1990
year_range = 3


def get_file_path(doi):
    path_dic = {"PhysRev": "PR", "PhysRevA": "PRA", "PhysRevB": "PRB", "PhysRevC": "PRC", \
        "PhysRevD": "PRD", "PhysRevE": "PRE", "PhysRevSeriesI": "PRI", "PhysRevLett": "PRL", \
        "PhysRevSTAB": "PRSTAB", "PhysRevSTPER": "PRSTPER", "PhysRevX": "PRX", "RevModPhys": "RMP"}

    doi = str(doi)
    subdoi = doi[8:]
    li = subdoi.split('.')
    journal = li[0]
    foldernum = li[1]
    path = os.path.join(base_path, path_dic[journal], foldernum, subdoi)
    path = path + '.json'
    return path


def get_year_by_doi(doi):
    path = get_file_path(doi)
    f = open(path, 'r')
    data = json.load(f)
    f.close()
    pub_year = data['date'][0:4]
    return int(pub_year)


def get_author_order_(doi, author):
    print "in get_author_order_", doi, author
    path = get_file_path(doi)
    f = open(path, 'r')
    data = json.load(f)
    f.close()
    authors = data['authors']
    count = 0
    flag = 0
    for au in authors:
        count += 1
        if repr(au['name'].encode('utf-8'))[1:-1] == author:
            author_order_weight = float(count) / len(authors)
            flag = 1
            break
    if flag:
        return float(count) / len(authors)
    else:
        print "error in get_author_order_ function:", doi, author
        exit()


def get_journal_by_doi(doi):
    subdoi = doi[8:]
    li = subdoi.split('.')
    journal = li[0]
    return journal

# get author's HITS value, save in author_authority_dic
author_authority_dic = {}
with open(r'..\paperauthorgraph\authority\authority20.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, dialect='excel')
    for row in reader:
        author = row[0]
        author_authority_dic[author] = float(row[1])
print "author_authority_dic over"
# print author_authority_dic.keys()
# exit()

# get journal's HITS value, save in journal_authority_dic
journal_list = ['PhysRev', 'PhysRevA', 'PhysRevB', 'PhysRevC', 'PhysRevD', 'PhysRevE',
                'PhysRevSeriesI', 'PhysRevLett', 'PhysRevSTAB', 'PhysRevSTPER', 'PhysRevX', 'RevModPhys']
journal_authority_dic = dict.fromkeys(journal_list, 1.0)
with open(r'..\paperjournalgraph\authority\authority20.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, dialect='excel')
    for row in reader:
        key = row[0]
        if journal_authority_dic.has_key(key):
            journal_authority_dic[key] = float(row[1])
print "journal_authority_dic over"

# get author list, save in author_li
author_li = []
with open(r'.\select_author_start_1990.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, dialect='excel')
    for row in reader:
        author = repr(row[0])[1:-1]
        author_li.append(author)
print "author_li over"
print len(author_li)

# get author_paper_dic, only contain the paper published 3 years after 1990.
author_paper_dic = {}
with open(r'.\new_author_paper_list.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, dialect='excel')
    for row in reader:
        author = repr(row[0])[1:-1]
        if author in author_li:
            paper_li = row[1][2:-2].split('\', \'')
            author_paper_dic[author] = paper_li
print "author_paper_dic over"
print len(author_paper_dic.keys())

# get paper_pagerank_value_dic
paper_pagerank_value_dic = {}
with open(r'..\papergraph\pagerankvalue.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, dialect='excel')
    for row in reader:
        paper_pagerank_value_dic[row[0]] = float(row[1])
print "paper_pagerank_value_dic over"

# calculate formular value, save in author_formular_value_dic
author_formular_value_dic = {}
for item in author_paper_dic.iteritems():
    formular_value_part = 0
    author = item[0]
    print "author:", author
    # print repr(author)[1:-1]
    paper_li = item[1]
    for doi in paper_li:
        tmp_value = 1.0
        year = get_year_by_doi(doi)
        if year in range(start_year, start_year + year_range):
            author_order = get_author_order_(doi, author)
            journal = get_journal_by_doi(doi)
            try:
                tmp_value = paper_pagerank_value_dic[doi] * journal_authority_dic[journal]
            except KeyError as e:
                pagerank_error_log = open(r'.\pagerank_error_range_%s.log' % year_range, 'a+')
                pagerank_error_log.write(str(author) + '  ' + str(doi) + '  ' + str(journal) + '\n')
                pagerank_error_log.close()
            formular_value_part += author_order * tmp_value
    try:
        formular_value = author_authority_dic[author] * formular_value_part
    except KeyError as e:
        error_log = open(r'.\error_range_%s.log' % year_range, 'a+')
        error_log.write(author + '\n')
        error_log.close()
    author_formular_value_dic[author] = formular_value

# save formular value in csv file
with open(r'.\formular_value_range_%s.csv' % year_range, 'wb') as csvfile:
    writer = csv.writer(csvfile, dialect='excel')
    writer.writerows(author_formular_value_dic.iteritems())
print "formular_value.csv write over"
