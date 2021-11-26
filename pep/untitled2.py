# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 15:38:14 2021

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



#Extraer las variables que quiero extraer
my_vars=['temp_celsius', 'cnt']



#Extraer las variables y salvarlas dentro de wbr_minimal
wbr_minimal = wbr[my_vars]
wbr_minimal.shape




wbr_2011 = wbr[wbr.yr == 0]
wbr_2011.shape



plt.hist(wbr_2011.cnt)
wbr_2011.cnt.describe()



#Ventasl del invierno del 2012



wbr_2012_inv = wbr[(wbr.yr == 1) & (wbr.season == 1)]
wbr_2012_inv



#Ventas de Invierno y Otono



wbr_invierno_fall = wbr[(wbr.season == 1) | (wbr.season == 4)]
wbr_invierno_fall.cnt.describe





#Cargando nuevo dataset




os.chdir(r'C:\Users\marta\git\Edem2021MDA\pep')
os.getcwd()



wbr = pd.read_csv ('wbr_ue.csv', sep=';', decimal=',')
wbr.shape



plt.hist(wbr.temp_celsius)



#Agrego columna reemplazando el numero 99 por nan



wbr['temp_celsius_c'] = wbr.temp_celsius.replace(99, np.nan)



plt.hist(wbr.temp_celsius_c)
wbr.temp_celsius_c.describe()



#Eliminando nan de todo el dataset (solo hacerlo si vamos a utilizar todos los datos)
wbr_ue2 = wbr.dropna ()
wbr_ue2.shape




##### Transformacion de datos ####



wbr['cs_ratio'] = (wbr.casual)/(wbr.registered) #Creando nueva columna con el valor calculado de dos variables



wbr.pop('cnt')



wbr['cnt_nuevo'] = wbr.casual + wbr.registered




#Recodificar
wbr.loc[(wbr['season'] == 1), 'season_cat'] = 'Winter'
wbr.loc[(wbr['season'] == 2), 'season_cat'] = 'Spring'
wbr.loc[(wbr['season'] == 3), 'season_cat'] = 'Summer'
wbr.loc[(wbr['season'] == 4), 'season_cat'] = 'Fall'





#Tabla cruzada
pd.crosstab(wbr.season, wbr.season_cat)



#Convertir variable numerica a texto



wbr.cnt_nuevo.describe()


reset -f




import os #sistema operativo
import pandas as pd #gestionar dataframes
import numpy as np # numeric python vectores
import matplotlib.pyplot as plt # graficos



os.chdir(r'C:\Users\marta\git\Edem2021MDA\pep')
os.getcwd()



wbr = pd.read_csv ('WBR_11_12_denormalized_temp.csv', sep=';', decimal=',')
wbr.shape




#Creando nueva columna con el valor calculado de dos variables



wbr['cs_ratio'] = (wbr.casual)/(wbr.registered)



#Recodificar
wbr.loc[(wbr['season'] == 1), 'season_cat'] = 'Winter'
wbr.loc[(wbr['season'] == 2), 'season_cat'] = 'Spring'
wbr.loc[(wbr['season'] == 3), 'season_cat'] = 'Summer'
wbr.loc[(wbr['season'] == 4), 'season_cat'] = 'Fall'




#Tabla cruzada
pd.crosstab(wbr.season, wbr.season_cat)



#Convertir variable numerica a texto




wbr.loc[(wbr['cnt'] < 2567), 'cnt_cat2'] = '1: Low_rentals'
wbr.loc[((wbr['cnt'] >= 2567) & (wbr['cnt'] < 6442)), 'cnt_cat2'] = '2: Average rental'
wbr.loc[(wbr['cnt'] >=6442), 'cnt_cat2'] = '3: High rentals'



#QC
plt.scatter(wbr.cnt, wbr.cnt_cat2, s=10)
plt.show()




#Graficar cnt_cat2
mytable = wbr.groupby(['cnt_cat2']).size()
mytable



n = mytable.sum()
mytable2 = (mytable/n)*100



print(mytable2)
mytable3 = round(mytable2,1)
mytable3



#Barchart



bar_list = ['1: Low rentals', '2: Average rental', '3: High rentals']
plt.bar(bar_list, mytable2,edgecolor='black')
plt.title('Figure1. Ventas')
plt.ylabel('Percentage')
#plt.text(1.7, 50, 'n: 731')
plt.show()



wbr.dtypes

#VARIABLE ORDINAL
#PRIMERO
# Import specific functionality
from pandas.api.types import CategoricalDtype
# First define a specific categorical data type specific for us!!! (in two sub-steps)
# Step 1: declare the ordered categories (DEFINO LA LISTA CON LAS CLASES)
my_categories=["Low rentals", "Average rentaL", "High rentals"]
#Step 2: Define new data type  NUEVO TIPO DE DATO. LAS CATEGORIAS LAS QUE HE GENERADO ANTERIORMENETE
my_rentals_type = CategoricalDtype(categories=my_categories, ordered=True)
# Second create a new categorical_ordered variable using our specific data type. Y DECIRLE, ADEMAS ESTA LISTA ESTA ORDENADA
wbr["cnt_cat5"] = wbr.cnt_cat2.astype(my_rentals_type)
wbr.info()

#AHORA VAMOS A USAR TODO ESTO, VOY A FORMZAR LA VARAIBLE Y A OBLIGARLE A QUE SE CONVIERTA EN EL TIPO QUE ACABAMOS DE DEFINIR ARRIBHA

plt.scatter(wbr.cnt, wbr.cnt_cat5, s=10)
plt.show()




#Graficar cnt_cat5
mytable = wbr.groupby(['cnt_cat5']).size()
mytable



n = mytable.sum()
mytable2 = (mytable/n)*100



print(mytable2)
mytable3 = round(mytable2,1)
mytable3



#Barchart



bar_list = ['1: Low rentals', '2: Average rental', '3: High rentals']
plt.bar(bar_list, mytable2,edgecolor='black')
plt.title('Figure1. Ventas')
plt.ylabel('Percentage')
#plt.text(1.7, 50, 'n: 731')
plt.show()






