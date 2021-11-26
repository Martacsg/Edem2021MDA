# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

3+2

a= 'good morning'
b= 'Vietnam'

print(a)
print(b)

c= a + b

print(c)

import os   #sistema operativo
import pandas as pd   #gestionar datframes
import numpy as np     # numeric python vectores
import matplotlib.pyplot as plt  # grafics

#create a dataframe 
#Lists are defined i Python whith [], separate by commas

name = ['Marta', 'Thais', 'Enrique', 'Lluna', 'Cristian']
age = [35,34,45,24,22]
gender = ['Female', 'Famale', 'Male', 'Female','Male']

print(name, age, gender)


class2021 = pd.DataFrame({'name' : name, 'age' : age, 'gender' : gender})

#clean up
del (age,gender,name)

del (a)
del (b)
del (c)

class2021.shape   #dimensionalidad de un dataframe

class2021.head(3)
class2021.tail(2)

#QC OK

edad = class2021.age
del(edad)


#Get working directory
os.chdir(r'C:\Users\marta\git\Edem2021MDA\pep')
os.getcwd()

#save dataframe to excel
class2021.to_excel("class2020.xlsx")
class2021.to_csv("class2020.csv")


#Reset all (carefull this is a "magic" funcion then it doesn´t)
reset -f

#Load basiclibraries
import os   #sistema operativo
import pandas as pd   #gestionar datframes
import numpy as np     # numeric python vectores
import matplotlib.pyplot as plt  # grafics

#change working directory
os.chdir(r'C:\Users\marta\git\Edem2021MDA\pep')
os.getcwd()



#to learn path to file:

rentals_2011 = pd.read_csv ('washington_bike_rentals_2011.csv', sep=';', decimal=',')

rentals_2011.shape
rentals_2011.head()
rentals_2011.tail()

#QC OK

#Extra our first plot
import matplotlib.pyplot as plt

#select  the variable to plot

rentals_2011.cnt
np.mean (rentals_2011.cnt)
np.std (rentals_2011.cnt)


rentals_2011.cnt.mean()    #en python
rentals_2011.cnt.describe()


plt.hist(rentals_2011.cnt)    #histograma
rentals_2011.cnt.hist()


#plot
x=rentals_2011.cnt   #si el nombre de la variable no tiene espacios
x=rentals_2011['cnt']   #cuando hay cararcteres especiales, espacios...

plt.hist(x,edgecolor='black', bins=20)
plt.xticks(np.arange(0, 7000, step=1000))
plt.title("Figure 1. Registred rental in Washington")
plt.ylabel('Frecuencia')
plt.xlabel('Number of rentals')
plt.show() #finalizar el gráfico

plt.hist(y,edgecolor='black')
ptl.show()

weather_2011 = pd.read_csv ('weather_washington_2011.csv', sep=';', decimal=',')

weather_2011.shape
weather_2011.dtypes

weather_2011.head()
weather_2011.tail()

#QC OK

del(x)

rental_weather_2011 =pd.merge(weather_2011, rentals_2011, on="day")

rental_weather_2011.shape



rental_weather_2011.to_csv("rental_weather_2011.csv")


del rental_weather_2011['dteday_y']    #borrar columna

#cambiar nombre columna
rental_weather_2011 =  rental_weather_2011.rename(columns={"dteday_x": "dteday"})

del (weather_2011)
del (rentals_2011)
del (class2021)

rentals_weather_2012= pd.read_csv ('rentals_weather_2012.csv', sep=';', decimal=',')

rentals_weather_2012.shape
rentals_weather_2012.head()
rentals_weather_2012.tail()

#QC ok

#añadimos filas del segundo fichero

rentals_weather_11_12 = rental_weather_2011.append(rentals_weather_2012, ignore_index=True)

#reordenar las columnas

#rentals_weather_11_12 = rentals_weather_11_12[rental_weather_2011.columns]

del(rental_weather_2011)
del(rentals_weather_2012)


wbr=rentals_weather_11_12
del(rentals_weather_11_12)


#describing a nominal variable
#Numerically
#frecuencies

mytable = wbr.groupby(['weathersit']).size()  #separo en grupos y le digo que me diga cuentos

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
bar_list = ['Sunny', 'Cloudy', 'Rainy']
plt.bar(bar_list, mytable2, edgecolor='black')
plt.bar(bar_list, mytable2)
plt.ylabel('Porcentage')
plt.xlabel('Weather')
plt.title('Figure1. Porcentaged weather situacions')
plt.text(1.7, 50,'n: 731')




plt.savefig('bar1.eps')  #Editable en Adove Ilustrator
plt.savefig('bar1.jpg')  #imagen tipo foto no ediable
plt.savefig('bar1.svg')  #Formato vectorial
plt.show()    #finalizar el gráfico

reset -f

import os   #sistema operativo
import pandas as pd   #gestionar datframes
import numpy as np     # numeric python vectores
import matplotlib.pyplot as plt  # grafics

os.chdir(r'C:\Users\marta\git\Edem2021MDA\pep')
wbr = pd.read_csv('WBR_11_12_denormalized_temp.csv', sep=';', decimal=',')

wbr.shape
wbr.head()
wbr.tail()

wbr.cnt
np.mean (wbr.cnt)
np.std (wbr.cnt)

wbr.cnt.describe()
x = wbr['cnt']

plt.hist(x, bins=10, edgecolor='black')
plt.xticks(np.arange(0, 10000, step=1000))

plt.title("Figure 1. Daily Bicycle rentals in Washinting")
plt.ylabel('Frecuency')
plt.xlabel('Number of rented bicycles')
plt.show() #finalizar el gráfico

res = wbr.cnt.describe()

res["mean"]
print(round (res[1],1))


m = res[1]
sd = res[2]
n = res[0]



plt.hist(x, bins=10, edgecolor='black')
plt.xticks(np.arange(0, 10000, step=1000))
plt.title('Figure 3. Daily Bicycle rentals in Washington DC' '\n''by Capital bikeshare. 2011 - 2012')
plt.ylabel('Frecuency')
plt.xlabel('Number of rented bicycles’)
props = dict(boxstyle='round', facecolor='white’,lw=0.5)
textstr = '$\mathrm{Mean}=%.1f$\n$\mathrm{S.D.}=%.1f$\n$\mathrm{n}=%.0f$'%(m, sd, n)
plt.text (6500,110, textstr , bbox=props)
plt.axvline(x=m,
linewidth=1,
linestyle= ('solid', color="red", label='Mean')






