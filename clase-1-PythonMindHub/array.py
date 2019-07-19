"""Genere dos vectores (listas o array):

1er vector llamado x con números enteros,

2do vector llamado y que contiene y=x+ε donde ε proviene de una distribución uniforme en el intervalo [0, 1].

Hint: use random.uniform"""
import random
x = [1,50,4]
print(x)

y = [x + [2]]
print (y)


y = [x + [random.uniform(0,1)]]
print (y)