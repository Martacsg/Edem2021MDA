# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 15:08:07 2021

@author: marta
"""

#rangos


import os   #sistema operativo
import pandas as pd   #gestionar datframes
import numpy as np     # numeric python vectores
import matplotlib.pyplot as plt  # grafics


os.chdir(r'C:\Users\marta\git\Edem2021MDA\pep')
os.getcwd()

wbr = pd.read_csv ('wbr_ue.csv', sep=',', decimal=',')

wbr .shape
wbr .head()
wbr .tail()


# Recode the number of rentals in three Groups
### Recode 1
wbr.loc[ (wbr['cnt']<2567.1) ,"cnt_cat2"]= "1: Low rentals"
wbr.loc[ ((wbr['cnt']>2567.1) & (wbr['cnt']<6441.6)) ,"cnt_cat2"]= "2: Average
rentals"
wbr.loc[ (wbr['cnt']>6441.6) ,"cnt_cat2"]= "3: High rentals"
##### Quality control?
plt.scatter(wbr.cnt, wbr.cnt_cat2, s=1)



mytable = wbr.groupby(['cnt']).size()  #separo en grupos y le digo que me diga cuentos

print(mytable)

mytable.sum()    #tabla, autosumate.

#PErcentages
n=mytable.sum()

mytable2 = (mytable/n)*100
print(mytable2)

mytable3 = round(mytable2,1)    #redondear 
mytable3


#Barchart1
#lets label the cathegories
bar_list = ['No Legendario', 'Legendario']
plt.bar(bar_list, mytable2, edgecolor='black')
plt.bar(bar_list, mytable2)
plt.ylabel('Porcentaje')
plt.xlabel('Clasificación')
plt.title('Figure3. Porcentaje Legendarios Pokemon')
plt.text(1.7, 20,'n: 800')
plt.savefig('bar3.eps')  #Editable en Adove Ilustrator
plt.savefig('bar3.jpg')  #imagen tipo foto no ediable
plt.savefig('bar3.svg')  #Formato vectorial
plt.show()    #finalizar el gráfico