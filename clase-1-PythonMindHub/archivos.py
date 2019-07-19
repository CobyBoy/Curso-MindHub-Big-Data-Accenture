"""1)Lea el archivo cereal.csv

Tome el header (nombre de cada columna) y guardelo en una lista"""
"""Usando colaboratory"""
from google.colab import files
uploaded = files.upload()


f = open('cereal.csv', 'r')
header = f.readline()
listaheader = header.split(',')
print (listaheader)

"""2) Lea cada una de las lineas del archivo guardando en listas diferentes cada dato relacionado con una columna en particular, o sea una lista para los elementos de la primera columna, otra lista para los elementos de la tercera columna, y asi sucesivamente.

(Utilice la funcion split de los string)"""

f = open('cereal.csv', 'r')
todo = f.readlines()
union =''
for elemento in todo:
  listita= elemento.split(',')
  for i in range(len(listita)):
    union += listita[i].split(' ')
print(union)

