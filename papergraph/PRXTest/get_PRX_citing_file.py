# -*- coding:utf-8 -*-
'''
@author:Zhong Peng
@createDate:2015-11-06
@lastModified:2015-11-06
@version:1.0.0
extract citing data of PRX that both the citing paper and cited paper are in PRX.
'''
import csv
import os
import json

def getAllFilePath(folder_path):
    '''get all json files' path and return a list'''
    final_file_path_list = []
    for root, dirs, files in os.walk(folder_path):
        for f in files:
            final_file_path_list.append(os.path.join(root, f))
    return final_file_path_list

def getAllDoiByPath(path_list):
    '''get all doi's list '''
    path_doi_dic = {}
    for file_path in path_list:
        f = open(file_path, 'r')
        data = json.load(f)
        f.close()
        if data.has_key('id'):
            doi = data['id'].encode('utf-8')
        else:
            continue
        if data.has_key('authors') and len(data['authors']) != 0:
            path_doi_dic[file_path] = doi
        else:
            continue
    return path_doi_dic

def extract_citation_data(citationFilePath, folderPath, newCitationFilePath):
    '''get citation data'''
    path_doi_dic = getAllDoiByPath(getAllFilePath(folderPath))
    doi_list = path_doi_dic.values()
    final_li = []    #store citing relation

    with open(citationFilePath, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if (row[0].encode('utf-8') in doi_list) and (row[1].encode('utf-8') in doi_list):
                final_li.append(row)
    print "file read over"

    with open(newCitationFilePath, 'wb') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(final_li)
    print "file write over"



if __name__ == '__main__':
    citationFilePath = r'aps-dataset-citations-2013.csv'
    folderPath = r'E:\APS-DATA\aps-dataset-metadata-2013\PRX'
    newCitationFilePath = r'PRX_citation.csv'
    extract_citation_data(citationFilePath, folderPath, newCitationFilePath)
