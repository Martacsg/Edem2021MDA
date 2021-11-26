# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 20:05:48 2021

@author: marta
"""
reset -f

import os #sistema operativo
import pandas as pd #gestionar dataframes
import numpy as np # numeric python vectores
import matplotlib.pyplot as plt # graficos
from pandas.api.types import CategoricalDtype #Gestionar variables ordinales
import scipy.stats as stats


os.chdir(r'C:\Users\marta\git\Edem2021MDA\pep')
os.getcwd()



wbr = pd.read_csv ('WBR_11_12_denormalized_temp.csv', sep=';', decimal=',')
wbr.shape



#1-Describe the two variables involved int th hypothesis
wbr.cnt.describe()
plt.hist(wbr.cnt)

mytable = wbr.groupby(['season']).size()
mytable
n = mytable.sum()

mytable2 = (mytable/n)*100

print(mytable2)
mytable3 = round(mytable2,1)
mytable3



bar_list = ['1: Winter', '2: Spring', '3: Summer', '4: Autumn']
plt.bar(bar_list, mytable2,edgecolor='black')
plt.title('Figure1. Ventas')
plt.ylabel('Percentage')
#plt.text(1.7, 50, 'n: 731')
plt.show()



#2-Perform the numeric test. la media de los working days es superior
wbr.groupby('season').cnt.mean()




#3-Perform the graphic test: plot of the mean


#4-When posible:


#Comparacion estadistica
# Subsetting
cnt_winter=wbr.loc[(wbr['season'] == 1), 'cnt'] # grupo 1, 'cnt'= variable cuantitativa a testear
cnt_spring=wbr.loc[(wbr['season'] == 2), 'cnt'] # grupo 2
cnt_summer=wbr.loc[(wbr['season'] == 3), 'cnt'] # grupo 3
cnt_autumn=wbr.loc[(wbr['season'] == 4), 'cnt'] # grupo 4

#import scipy.stats as stats  #pvalue
res=stats.f_oneway(cnt_winter, cnt_spring, cnt_summer, cnt_autumn)
print(res)


print('F:', round(res[0],3), 'P.Value')



#Grafic comparison: cofidence intervals for the means
import seaborn as sns
import matplotlib.pyplot as plt 

#CI meanplot version1: básica
#ax = sns.pointplot(x="weathersit", y="cnt", data=wbr,ci=95, join=0)


#CI meanplot version2
ax = sns.pointplot(x="season", y="cnt", data=wbr,ci=95, join=0)
plt.axhline(y=wbr.cnt.mean(),   #pintamos la liea de la media
            linewidth=1,
            linestyle= 'dashed',
            color="green")  #color de la linea de l amedia
ax.set_ylabel('Rentals')
plt.yticks(np.arange(1000, 7000, step=500))
plt.ylim(0,7000) #rango entre 0 y 9.000

props = dict(boxstyle='round', facecolor='white', lw=0.5)
plt.text(1.5,5000,'Mean:4504.3''\n''n:731' '\n' 't:1.601' '\n' 'Pval.:0.000', bbox=props)
plt.xlabel('Season')
plt.title('Figure 6. Average rentals by Season.''\n')




#boxplot
ax = sns.boxplot(x="season", y="cnt", data=wbr)
