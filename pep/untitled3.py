# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 17:24:38 2021

@author: marta
"""

reset -f

import os #sistema operativo
import pandas as pd #gestionar dataframes
import numpy as np # numeric python vectores
import matplotlib.pyplot as plt # graficos



os.chdir(r'C:\Users\marta\git\Edem2021MDA\pep')
os.getcwd()


wbr = pd.read_csv ('WBR_11_12_denormalized_temp.csv', sep=';', decimal=',')
wbr.shape
wbr .head()
wbr .tail()


wbr.workingday
np.mean (wbr.workingday)
np.std (wbr.workingday)

wbr.workingday.mean()    #en python
wbr.workingday.describe()


plt.hist(wbr.workingday)    #histograma
wbr.workingday.hist()
plt.show()


x=wbr.workingday   #si el nombre de la variable no tiene espacios
x=wbr['workingday']   #cuando hay cararcteres especiales, espacios...

plt.hist(x,edgecolor='black', bins=20)
plt.xticks(np.arange(0, 2, step 1000)
plt.title("Figura 1. La velocidad")
plt.ylabel('Frecuencia')
plt.xlabel('Velocidad')
plt.savefig('bar1.eps')  #Editable en Adove Ilustrator
plt.savefig('bar1.jpg')  #imagen tipo foto no ediable
plt.savefig('bar1.svg')  #Formato vectorial
plt.show()

#Describir variable
#Rentals
wbr.groupby('wd_cat')cnt.describe()
wbr.groupby('wd_cat')cnt.mean()


#Test
#Gráfico

