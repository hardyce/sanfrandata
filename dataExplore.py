# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 22:47:51 2016

@author: hardy_000
"""
import sexmachine.detector as gender
import pandas as pd
path="C:\\Users\\hardy_000\\Documents\\SanFranSal\\Salaries.csv"
data=pd.read_csv(path)
data.columns = map(str.lower, data.columns)


d = gender.Detector()
firstname=data.employeename.apply(lambda x: x.partition(' ')[0])
firstname=firstname.str.lower()
firstname=firstname.str.title()
gender=firstname.apply(lambda row: d.get_gender(row))
