# -*- coding:utf-8 -*-
'''
create new citation file in csv format that exclude doi that doesn't have complete data.
(e.g. there're some files lacking of author data)
Here we need doi, publicate year, authors, first author's affiliation and journal info.
'''
import os
import csv
import json

def getAllFilePath(folder_path):
    '''get all json files' path and return a list'''
    print "Function getAllFilePath Start"
    final_file_path_list = []
    for root, dirs, files in os.walk(folder_path):
        for f in files:
            final_file_path_list.append(os.path.join(root, f))
    print "Function getAllFilePath end"
    return final_file_path_list

def getFullInfoDoiList(file_path_list):
    '''input param is all json file's path list, and return is a doi list that 
    doi's all info is complete.'''
    print "Function getFullInfoDoiList Start"
    doi_list = []
    for file_path in file_path_list:
        # print file_path
        f = open(file_path, 'r')
        data = json.load(f)
        f.close()
        if not(data.has_key('date')):
            continue
        if not(data.has_key('authors')):
            continue
        else:
            author_list = data['authors']
            if not(author_list[0].has_key('affiliationIds')):
                continue
            else:
                if author_list[0]['affiliationIds'] == '':
                    continue
        doi = data['id'].encode('utf-8')
        doi_list.append(doi)
    print "Function getFullInfoDoiList end"
    return doi_list

def createNewCitationFile(doi_list, old_citation_file_path, new_citation_file_path):
    '''create new citation file'''
    print "Function createNewCitationFile Start"
    new_citation_list = []
    with open(old_citation_file_path, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if (row[0] in doi_list) and (row[1] in doi_list):
                new_citation_list.append(row)
    print "File read and process over"
    with open(new_citation_file_path, 'wb') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(new_citation_list)
    print "File write over"
    print "Function createNewCitationFile end"

if __name__ == '__main__':
    folder_path = r'E:\APS-DATA\aps-dataset-metadata-2013'
    old_citation_file_path = r'E:\APS-DATA\aps-dataset-citations-2013\aps-dataset-citations-2013.csv'
    new_citation_file_path = r''
    file_path_list = getAllFilePath(folder_path)
    doi_list = getFullInfoDoiList(file_path_list)
    createNewCitationFile(doi_list, old_citation_file_path, new_citation_file_path)
