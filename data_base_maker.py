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


def work_dict(base):
    data = {}
    if base[0] not in data.keys():
        data[base[0]] = {'old_res': [], 'new_res': []}
    data[base[0]]['old_res'].append(base[1])
    data[base[0]]['new_res'].append(base[2])
    return data


def first_step(raw_data, po):
    pool = []
    data = []
    for key in raw_data.keys():
        for x in raw_data[key]:
            for y in [3,4,5]:
                work = po.cell(row=x, column=y).value
                data.append(work)
            pool.append(work_dict(data))
            data.clear()
        raw_data[key] = [*pool]
        print(pool)
        pool.clear()
    return raw_data


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


            
raw_data = first_step(raw_data,sheet)  




for key in raw_data.keys():
    print(raw_data[key])

        


    