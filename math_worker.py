#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 12:55:14 2019

@author: fireet
"""
from data_base_maker import get_data


class Complex:
    ind = []

    def __init__(self,
                 complex_name='',
                 hot_water_tar=0.0,
                 cold_water_tar=0.0,
                 electro_tar=0.0,
                 water_off_tar=0.0
                 ):

        self.complex_name = complex_name
        self.hot_water_tar = hot_water_tar
        self.cold_water_tar = cold_water_tar
        self.water_off_tar = water_off_tar
        self.electro_tar = electro_tar
        self.arend = []
        Complex.ind.append(self)

    def add_arend(self, doc, name):
        tars = dict(ГВС=self.hot_water_tar,
                    ХВС=self.cold_water_tar,
                    ЭЭ=self.electro_tar,
                    ОТВОД=self.water_off_tar)
        self.arend.append(Arend(doc=doc, name=name, tars=tars))


class Res:
    def __init__(self,
                 name='',
                 old=0.0,
                 new=0.0,
                 coef=1.0,
                 tars={}):

        self.name = name
        self.old = old
        self.new = new
        self.total = 0.0
        self.tars = tars[name.split()[0].upper()]
        self.coef = coef
        self.cash = 0.0

    def work_res(self):
        self.total = round(self.new - self.old)
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
        self.data_res = {}
        self.tars = tars
        Arend.arend_pool.append(self)

    def new_res(self,
                name_res='',
                old=0.0,
                new=0.0,):

        self.data_res[name_res] = Res(name=name_res,
                                      old=old,
                                      new=new,
                                      tars=self.tars)



names = [dict(complex_name='first',
              hot_water_tar=13.25,
              cold_water_tar=0.0,
              water_off_tar=14.29,
              electro_tar=0.0,
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

for item in names:
    Complex(**item)

x = Complex.ind[0]
x.add_arend('doc', 'name')
print(x.arend[0].tars)

data = get_data()