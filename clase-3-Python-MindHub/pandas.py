
"""Usaremos un dataset llamado "conjunto de datos iris de Fisher" que trae caracteristicas (ancho y largo de sepalos y petalos) de varias muestras provenientes de 3 especies especies distintas.

Para traernos el dataset, importamos la data mediante la libreria sklearn, que se utiliza para implementar algoritmos de machine learning"""
from sklearn.datasets import load_iris
iris = load_iris()
"""observamos los elementos que tenemos como llaves"""
iris.keys()
import pandas as pd
"""empezamos definiendo un dataframe con las caracteristicas"""
df_1 = pd.DataFrame(iris['data'], columns= iris['feature_names'])
df_1.head(3)
"""y otro dataframe con las etiquetas, en estas etiquetas estan codificada la especia a la cual pertenece cada planta"""
df_2 = pd.DataFrame(iris['target'], columns=['name'])
df_2.head(3)
df_2['name'].unique()
"""Y en esta celda los nombres de cada especie por orden de indice, o sea 0 es setosa, 1 es versicolor, 2 es virginica"""
iris['target_names']
"""1) decodificar en df_2 el nombre de cada especie, esto es, reemplazar los numeros, por los nombres dados en target name, en df_2"""
df_2['name'] = df_2['name'].apply(lambda x:iris['target_names'] [x])
df_2
"""2) Hacer un join entre df_1 y df_2, ambos dataframes se encuentran ordenados llame a este nuevo dataframe df"""
df = df_1.join(df_2)
df.sample(5)
"""3) ¿Cuantas filas y cuantas columnas tiene el dataframe df?"""
df.shape

"""¿que tipo de dato es la 4ta columna?,¿ cual es el tipo de dato de la 3ra?"""
df.dtypes[4]
df['name'].dtype
"""¿Cuanto espacio ocupa el dataframe?"""
df.info()
"""6) Genere una columna area, que estime el area tomando el cuenta el ancho y largo de los sepalos"""
df.iloc[:,1]
df['area']=df.iloc[:,0]*df.iloc[:,1]
df
"""7) ¿Cual es la media de tamaño de esa area?"""
df['area'].mean()
"""8) ¿Cual es la media de esa area por especie? (groupby)"""
df.groupby('name').agg('mean')

