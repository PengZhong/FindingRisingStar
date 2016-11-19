# -*- coding: utf-8 -*-
"""
author: Zhong Peng
createDate: 2015-12-04
根据author_start_end_year.csv选取起始年份在某一时间段内，终止年份在某一年的作者并生成文件
第一列为作者名，第二列为起始年份，第三列为终止年份
"""
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

start_year_left = 1990
end_year_left = 1995
end_year = 2013

final_li = []
with open(r'.\author_start_end_year.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, dialect='excel')
    for row in reader:
        tmp_li = []
        author = row[0]
        start_year = int(row[1])
        end_year = int(row[2])
        # print start_year, end_year
        if 1990 <= start_year <= 1995 and end_year == 2013:
            tmp_li.append(author)
            tmp_li.append(start_year)
            tmp_li.append(end_year)
            final_li.append(tmp_li)

with open(r'.\select_author.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, dialect='excel')
    writer.writerows(final_li)