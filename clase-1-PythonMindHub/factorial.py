"""1) Escriba una función  factorial(n)  que para cualquier número natural  n  devuelve  n!"""
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print(fact)

factorial(5)


"""2) Reuse la función anterior en una nueva función que ahora devuelva  n!−k  para cualquier entero  n  con  k  parametrizable y fijado por defecto en  1 ."""
def factorial2(n,k=1):
    fact = 1
    for i in range(1,n+1):
        fact= fact*i
    print(fact-k)