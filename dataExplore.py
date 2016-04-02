# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 22:47:51 2016

@author: hardy_000
"""
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import sexmachine.detector as gender
import pandas as pd
import numpy as np
path="C:\\Users\\hardy_000\\Documents\\SanFranSal\\Salaries.csv"
data=pd.read_csv(path)
data.columns = map(str.lower, data.columns)


d = gender.Detector()
firstname=data.employeename.apply(lambda x: x.partition(' ')[0])
firstname=firstname.str.lower()
firstname=firstname.str.title()
gender=firstname.apply(lambda row: d.get_gender(row))
gender[gender=="andy"]="unknown"
data["sex"]=gender
genderGroup=data.groupby(["sex","year"])
data["basepay"]=pd.to_numeric(data["basepay"],errors="coerce")
data=data.fillna(0)
men=data[(data["sex"]=="male") | (data["sex"]=="mostly_male")]
women=data[(data["sex"]=="female") | (data["sex"]=="mostly_female")]
data["basepay"] = data["basepay"].replace('[^0-9]+.-', '', regex=True)

f, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 4))
sns.distplot(men.basepay, bins = 50, kde=False,ax=ax1)
sns.distplot(women.basepay, bins = 50, kde=False,ax=ax2)

