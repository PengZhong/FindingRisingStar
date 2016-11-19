# -*- coding:utf-8 -*-
'''
@author:Zhong Peng
@createDate:2015-11-08
@version:1.0.0
create file that include paper author info.
(only the paper in the new_aps_citations-2013.csv will be included)
'''
import csv

def get_doi_set(new_citation_file_path):
    '''return a set of doi that in new_aps_citations-2013.csv 
    where dois in this file's info is complete'''
    print 'Function get_doi_set start'
    doi_set = set()
    with open(new_citation_file_path, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            doi_set.add(row[0].encode('utf-8'))
            doi_set.add(row[1].encode('utf-8'))
    print 'Function get_doi_set end'
    return doi_set

def create_new_paper_author_file(doi_set, old_paper_author_file_path, new_author_paper_file_path):
    '''create new paper_author_file'''
    print 'Function create_new_paper_author_file start'
    new_paper_author_li = []

    tmp_li = []
    with open(old_paper_author_file_path, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            doi = row[0].encode('utf-8')
            if doi in doi_set:
                author_li = row[1][2:-2].split("', '")
                for author in author_li:
                    tmp_li = []
                    tmp_li.append(doi)
                    tmp_li.append(author)
                    new_paper_author_li.append(tmp_li)
    print 'Old paper_author file read over'

    with open(new_author_paper_file_path, 'wb') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(new_paper_author_li)
    print 'New paper_author file write over'
    print 'Function create_new_paper_author_file end'

if __name__ == '__main__':
    new_citation_file_path = r'..\papergraph\new_aps_citations-2013.csv'
    old_paper_author_file_path = r'new_paper_author_all.csv'
    new_author_paper_file_path = r'new_paper_author.csv'
    doi_set = get_doi_set(new_citation_file_path)
    create_new_paper_author_file(doi_set, old_paper_author_file_path, new_author_paper_file_path)


