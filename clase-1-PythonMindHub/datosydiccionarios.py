"""1) Itere sobre el siguiente diccionario d en la celda, para construir un nuevo diccionario que únicamente contenga los valores numéricos (enteros o flotantes) y cadenas del diccionario anterior. En particular este nuevo diccionario debe ser igual a:"""

"""resultado = {'num_0': 2, 'num_1': 3.14, 'str_0': 'henry', 'str_1': 'iv', 'num_2': 5}

Hint: use la función isinstance"""


d = {'a': 2, 'b': 3.14, 'c': 'henry', 'd': 'iv', 'e': 5, 'f': None, 'g': []}

listnum = []
e = {}
for val in d.values():
  esent = isinstance(val, int)
  esfloat = isinstance(val, float)
  if esent | esfloat:
    listnum.append(val)
for val in range(len(listnum)):
  for elemento in listnum:
    e['num_']= elemento
print(e)