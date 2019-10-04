#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 13:29:04 2019

@author: fireet
"""

import data_base_maker as dbm
import pandas as pd
res = ['ХВС', 'ГВС', 'ЭЭ']
file_name = './data/59322001.xlsx'
working_area = dbm.get_dict_main(file_name)
print(working_area)

doc_list = [x for x in working_area]
names_list = [working_area[s].pop('name') for s in doc_list]
print(working_area)
for x in doc_list:
    for z in working_area[x]:
        print(z.split())
        if z.split()[0] in res:
            pass
