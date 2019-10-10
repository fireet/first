#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 12:55:14 2019

@author: fireet
"""
from data_base_maker import get_data, get_complex_tars
from pandas import DataFrame

class Complex:
    ind = {}

    def __init__(self,
                 complex_name='',
                 hot_water_tar=0.0,
                 cold_water_tar=0.0,
                 electro_tar=0.0,
                 water_off_tar=0.0,
                 ):

        self.complex_name = complex_name
        self.hot_water_tar = hot_water_tar
        self.cold_water_tar = cold_water_tar
        self.water_off_tar = water_off_tar
        self.electro_tar = electro_tar
        self.arend = {}
        Complex.ind[complex_name] = self

    def add_arend(self, doc, name):
        tars = dict(ГВС=self.hot_water_tar,
                    ХВС=self.cold_water_tar,
                    ЭЭ=self.electro_tar,
                    ОТВОД=self.water_off_tar)
        self.arend[str(doc)] = (Arend(doc=str(doc),
                                      name=name,
                                      tars=tars))


class Res:
    def __init__(self,
                 name='',
                 old=0.0,
                 new=0.0,
                 coef=1.0,
                 tars={}):

        self.name = name.split()[0].upper()
        self.old = old
        self.new = new
        self.total = 0.0
        self.tars = tars[self.name]
        self.coef = coef
        self.cash = 0.0

    def work_res(self):
        self.total = round(self.new - self.old, 4)
        self.cash = round(self.total*self.coef*self.tars, 2)


class Arend:
    arend_pool = []

    def __init__(self,
                 doc='',
                 name='',
                 tars={}):

        self.doc = str(doc)
        self.name = name
        self.total_cash = 0.0
        self.data_res = []
        self.tars = tars
        Arend.arend_pool.append(self)

    def new_res(self,
                name_res='',
                old=0.0,
                new=0.0,
                coef=1.0):

        self.data_res.append(Res(name=name_res,
                                 old=old,
                                 new=new,
                                 tars=self.tars,
                                 coef=coef))

    def get_all_value(self):
        pool = {}
        total_cash_res = 0
        for i in self.data_res:
            if i.name not in pool:
                pool[i.name] = 0
            pool[i.name] += i.cash
            total_cash_res += i.cash
            self.total_cash += i.cash
        self.data_res.append(pool)


names = [dict(complex_name='first',
              hot_water_tar=13.25,
              cold_water_tar=13.82,
              water_off_tar=14.29,
              electro_tar=73.6,
              ),
         dict(complex_name='3rd',
              hot_water_tar=24.46,
              cold_water_tar=17.82,
              water_off_tar=14.29,
              electro_tar=200,
              ),
         dict(complex_name='2nd',
              hot_water_tar=13.25,
              cold_water_tar=0.0,
              water_off_tar=14.29,
              electro_tar=0.0,
              ),
         ]

names = get_complex_tars()
print(names)

Complex(**names['первый'])
active = Complex.ind['первый']

data = get_data()
for item in data:
    if item[0] not in active.arend and item[0]:
        name = item[1]
        doc = item[0]
        active.add_arend(doc, name)
    tmp = dict(name_res=item[2],
               old=item[3],
               new=item[4],
               coef=item[5],
               )
    active.arend[str(doc)].new_res(**tmp)
    for i in active.arend[str(doc)].data_res:
        i.work_res()
for x in active.arend.values():
    x.get_all_value()
    
for x in Complex.ind.values():
    for s in x.arend.values():
        print(s.__dict__)