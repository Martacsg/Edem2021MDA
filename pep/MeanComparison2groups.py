# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 18:29:06 2021

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
#Rentals
wbr.cnt.describe()
plt.hist(wbr.cnt)


mytable = wbr.groupby(['yr']).size()
mytable



n = mytable.sum()
mytable2 = (mytable/n)*100



print(mytable2)
mytable3 = round(mytable2,1)
mytable3



bar_list = ['1: 2011', '2: 2012']
plt.bar(bar_list, mytable2,edgecolor='black')
plt.title('Figure1. Ventas')
plt.ylabel('Percentage')
#plt.text(1.7, 50, 'n: 731')
plt.show()



#2-Perform the numeric test. la media de los working days es superior
wbr.groupby('yr').cnt.mean()




#3-Perform the graphic test: plot of the mean


#4-When posible:


#Comparacion estadistica
# Subsetting
cnt_wd=wbr.loc[(wbr['yr'] == 1), 'cnt'] # grupo 1, 'cnt'= variable cuantitativa a testear
cnt_nwd=wbr.loc[(wbr['yr'] == 0), 'cnt'] # grupo 2

#import scipy.stats as stats  #pvalue
res=stats.ttest_ind(cnt_wd, cnt_nwd, equal_var = False)
print(res[1])

("{:.%df}" % number_of_digits(result[1])).format(result[1])

#Grafic comparison: cofidence intervals for the means
import seaborn as sns
import matplotlib.pyplot as plt 

#CI meanplot version1: básica
ax = sns.pointplot(x="yr", y="cnt", data=wbr,ci=95, join=0)


#CI meanplot version2
ax = sns.pointplot(x="yr", y="cnt", data=wbr,ci=95, join=0)

plt.axhline(y=wbr.cnt.mean(),   #pintamos la liea de la media
            linewidth=1,
            linestyle= 'dashed',
            color="green")  #color de la linea de l amedia
ax.set_ylabel('Rentals')
plt.yticks(np.arange(3000, 7000, step=500))
plt.ylim(2800,7000) #rango entre 0 y 9.000

props = dict(boxstyle='round', facecolor='white', lw=0.5)
plt.text(0.1,6000,'Mean:4504.3''\n''n:731' '\n' 't:1.601' '\n' 'Pval.:0.000', bbox=props)
plt.xlabel('Year')
plt.title('Figure 6. Average rentals by year.''\n')