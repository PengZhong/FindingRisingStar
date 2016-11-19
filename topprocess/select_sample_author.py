# -*- coding: utf-8 -*-
"""
author: Zhong Peng
createDate: 2015-12-10
"""
import csv
all_row = list()
with open(r'.\author_career_gt20_citation_count.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, dialect='excel')
    for row in reader:
        all_row.append(row)

positive_row = list()
for row in all_row[:500]:
    positive_row.append(row)

negative_row = list()
for row in all_row[-500:]:
    negative_row.append(row)

with open(r'.\positive_author_sample.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, dialect='excel')
    writer.writerows(positive_row)

with open(r'.\negative_author_sample.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, dialect='excel')
    writer.writerows(negative_row)

