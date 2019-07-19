"""1) Escriba una función que recibe como argumentos dos secuencias (listas, tuplas o cadenas) y devuelve True (False) en caso que la primer secuencia este (no este) contenida en la segunda. No use conjuntos para esto."""


def sequence(lst,lst2):
  lst_insp=[]
  for elemento in lst:
    if elemento == lst2:
      lst_insp.append("encontro")
      print(lst_insp)
    else:
      lst_insp.append("no encontro")
      print(lst_insp)
      
  return "encontro" in lst_insp

list2 = ["d", "e"]
list1 = ["a", "b", list2, "c"]

sequence(list1, list2)
list2 = ["d", "e"]
list1 = ["a", "b", list2, "c"]
​
sequence(list1, list2)


"""2) Repita el ejercicio anterior pero usando conjuntos."""


def seq_set (lista1, lista2):
  return lista2 in lista1
 

list2 = ["d", "e"]
list1 = ["a", "b", list2, "c"]
​
seq_set(list1, list2)