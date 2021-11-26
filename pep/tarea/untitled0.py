# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 19:42:43 2021

@author: marta
"""



import os   #sistema operativo
import pandas as pd   #gestionar datframes
import numpy as np     # numeric python vectores
import matplotlib.pyplot as plt  # grafics


os.chdir(r'C:\Users\marta\git\Edem2021MDA\pep\tarea')
os.getcwd()

pokemon = pd.read_csv ('pokemon_data.csv', sep=',', decimal=',')

pokemon .shape
pokemon .head()
pokemon .tail()

pokemon.Speed
np.mean (pokemon.Speed)
np.std (pokemon.Speed)

pokemon.Speed.mean()    #en python
pokemon.Speed.describe()


plt.hist(pokemon.Speed)    #histograma
pokemon.Speed.hist()
plt.show()


x=pokemon.Speed   #si el nombre de la variable no tiene espacios
x=pokemon['Speed']   #cuando hay cararcteres especiales, espacios...

plt.hist(x,edgecolor='black', bins=20)
plt.xticks(np.arange(0, 180, step=50))
plt.title("Figura 1. La velocidad")
plt.ylabel('Frecuencia')
plt.xlabel('Velocidad')
plt.savefig('bar1.eps')  #Editable en Adove Ilustrator
plt.savefig('bar1.jpg')  #imagen tipo foto no ediable
plt.savefig('bar1.svg')  #Formato vectorial
plt.show()






pokemon.Defense
np.mean (pokemon.Defense)
np.std (pokemon.Defense)
pokemon.Defense.mean()    #en python
pokemon.Defense.describe()

y=pokemon.Defense   #si el nombre de la variable no tiene espacios
y=pokemon['Defense']   #cuando hay cararcteres especiales, espacios...

plt.hist(x,edgecolor='black', bins=20)
plt.xticks(np.arange(0, 230, step=50))
plt.title("Figura 2. La Capacidad Defensiva ")
plt.ylabel('Frecuencia')
plt.xlabel('Capacidad Defensiva')
plt.savefig('bar2.eps')  #Editable en Adove Ilustrator
plt.savefig('bar2.jpg')  #imagen tipo foto no ediable
plt.savefig('bar2.svg')  #Formato vectorial
plt.show()
#4) Describe numérica y gráficamente las variables nominales.




mytable = pokemon.groupby(['Legendary']).size()  #separo en grupos y le digo que me diga cuentos

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


mytable = pokemon.groupby(['Generation']).size()  #separo en grupos y le digo que me diga cuentos

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
bar_list = ['Primera', 'Segunda','Tercera', 'Cuarta', 'Quinta', 'Sexta']
plt.bar(bar_list, mytable2, edgecolor='black')
plt.bar(bar_list, mytable2)
plt.ylabel('Porcentaje')
plt.xlabel('Generación')
plt.title('Figure 4. Porcentaje Generación Pokemon')
plt.text(1.7, 20,'n: 800')
plt.savefig('bar4.eps')  #Editable en Adove Ilustrator
plt.savefig('bar4.jpg')  #imagen tipo foto no ediable
plt.savefig('bar4.svg')  #Formato vectorial
plt.show()    #finalizar el gráfico

#5) Presenta tus resultados de los puntos 3 y 4 en un breve informe.:
