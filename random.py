# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 21:36:14 2019

@author: Angel
"""
import random
import numpy as np  #para el uso de randint

#radint
#Si quisiéramos un entero aleatorio, podemos usar la función 
#randint Randint acepta dos parámetros: un número más bajo y un número más alto. 
#Generar enteros entre 1,5. El primer valor debe ser menor que el segundo.
print (random.randint(0, 5))

#Random
#Si desea un número mayor, puede multiplicarlo. 
#Por ejemplo, un número aleatorio entre 0 y 100:
print(random.random() * 100)

#choice
#La función de elección a menudo se puede usar para elegir un elemento 
#aleatorio de una lista.
myList = [2, 109, False, 10, "Lorem", 482, "Ipsum"]
print(random.choice(myList))

#shuffle
#La función aleatoria, baraja los elementos de la lista en su lugar, 
#por lo que están en un Orden aleatorio.
from random import shuffle
x = [[i] for i in range(10)]
shuffle(x)
print(x)

#Randrange
#Generar un elemento seleccionado al azar del rango (inicio, parada, paso)
#random.randrange (inicio, parada [, paso])
for i in range(3):
    print( random.randrange(0, 101, 5))

#numpy.random.randint(low(menor valor tomado), high=None(mayor valor tomado), 
#                           size=None(matriz (a,b,c)), dtype='l')
a=np.random.randint(2, size=10) #size=(1,10) #si no se pone size se asume que es el high
print(a)
print("##################")
f=np.random.randint(5, size=(2,4))
print(f)
print("####################")
c=np.random.randint(5, size=(2,4,3))
print(c)
print("##################")
d=np.random.randint(5, 10, 20)      #por defecto se asume : size=20
print(d)

#randn
print(np.random.randn())

#







