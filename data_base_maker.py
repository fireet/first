#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 13:40:04 2019

@author: fireet
"""

from openpyxl import load_workbook
file = './data/59322001.xlsx'


wb = load_workbook(file)
i = wb.sheetnames[0]

sheet = wb[i]


def get_dict(database):
    data = {}
    pool = []
    tmp = None
    for i in range(4, database.max_row+1):
        work = database.cell(row=i, column=2).value
        if work:
            if tmp:
                data[tmp] = [*pool]
            tmp = work
            pool.clear()
            pool.append(i)
            continue
        pool.append(i)
    return data


raw_data = get_dict(sheet)


def working_dict(data, database):
    pool = {}
    for key in data:
        if key not in pool:
            pool[key] = {}
        tmp = []
        s = {}
        for i in data[key]:
            for y in (3, 4, 5):
                work = database.cell(row=i, column=y).value
                tmp.append(work)
            if tmp[0] not in s:
                s[tmp[0]] = tmp[1:]

            tmp.clear()
        pool[key] = s.copy()
        s.clear()
    return pool

data_dict = working_dict(raw_data, sheet)
print(data_dict)
        