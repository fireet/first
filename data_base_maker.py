#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 13:40:04 2019

@author: fireet
"""

import openpyxl

settings = {
            'doc': 0,
            'name': 1,
            'indicator': 2,
            'old': 3,
            'new': 4,
            'tars': {
                    'ГВС': 12.13,
                    'ХВС': 9.52,
                    'ЭЭ': 134.164,
                    },
            }
            
wb = openpyxl.load_workbook('./data/59322001.xlsx')

work = wb.active
data = []
for row in range(4,work.max_row+1):
    tmp = []
    for column in range(1,6):
        tmp.append(work.cell(row,column).value)
    data.append(tmp)

tar = 2
old = 3
new = 4
result = 5

for item in data:
    x,y = item[old], item[new]
    answer = y-x
    item.append(round(answer,2))
    key = item[tar].split()[0]
    if key in settings['tars']:
        answer = item[result]*settings['tars'][key]
        item.append(round(answer,2))

def get_data():
    return data




def get_cell(key, data):
    pass