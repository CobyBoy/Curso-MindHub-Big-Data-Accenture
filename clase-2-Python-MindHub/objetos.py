"""1) Defina una clase Animal con las siguientes caracteristicas

Al instanciar debe pedir los parametros cuyos atributos deben formar parte del objeto:

atributo "nombre"

atributo "peso"

atributo "altura"

atributo "velocidad"

Calcular los siguientes atributos al instanciar

atributo potencial_de_ataque que es igual a  altura2+evelocidad−peso/2 

atributo potencial_de_defensa  peso3+altura∗2 
atributo vida

implemetar los metodos,

probabilidad_de_huida, como un numero aleatorio entre 0 y 1 (utilizar la libreria estandar random )

calcular_potencial_de_ataque calcular_potencial_de_defensa"""

from random import uniform
from math import exp
class Animal:
  def __init__(self,nombre, peso,altura,velocidad):
    self.nombre = nombre
    self.peso = peso
    self.altura = altura
    self.velocidad = velocidad
    self.vida = None
    self.pot_ataque = self.calc_p_a()
    self.pot_defense = self.calc_p_d()
  
  def calc_p_a(self):
    return self.altura**2 + exp(self.velocidad) - self.peso/2
  
  def calc_p_d(self):
    return peso**3 + self.altura*2
  
  def probabilidad_huida(self):
    return uniform(0,1)


"""2) Implemente una clase que herede de Animal y de Human inicializando todos los atributos declarados explicitamente"""
class Human:
    
    """Friendly human with a name."""

    def __init__(self, name):
        self.name = name
    
    def greet(self):
        
        print(f"Hi! My name is {self.name}")

class Humita (Animal, Human):
  
  def __init__(self, name,**kwargs):
    super().__init__(**kwargs)
    self.name = name

"""3)Implementar una clase que herede de Walk y de Animal y cuya representacion informe cuanto le falta por caminar (ver atributo meters, y atributo velocidad)

tiene que implementar el metodo demora(), que en funcion de la velocidad, calcule cuanto va a demorar en llegar, suponiendo la velocidad como metros por segundo.

Implemente los metodos para utilizar los simbolos  ><==  como comparadores del tiempo en que demora en llegar cada instancia de la clase que implemento"""

class Walk:
  
  def __init__(self, meters):
    self.trajectory = meters
  
  def walk(self):
    print(f'I walk {self.trajectory} meters')
    self.trajectory = 0
    self.otro =10
    return "done"

class CaminAnimal (Walk, Animal):
  
  def __init__(self, segundo, **kwargs):
    super().__init__(**kwargs)
    self.segundo = segundo
    
    def demora(self, velocidad, meters):
      return self.meters/self.segundo