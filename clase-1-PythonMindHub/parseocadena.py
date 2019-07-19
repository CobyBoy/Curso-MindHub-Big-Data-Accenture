"""1) Obtenga todos los caracteres en posición par de la cadena H1e2l3l4o5w6o7r8l9d"""
cadena = "H1e2l3l4o5w6o7r8l9d"
union=''
for i in range(len(cadena)):
    if i%2 == 0:
      union+=cadena[i]
print(union)   

"""2) Usando (varios) list comprehensions elimine todos los valores numéricos de la cadena y devuelve luego una nueva cadena idéntica a la del inciso anterior."""
charac = [i for i in cadena if i.isalpha()]
print (''.join(charac))