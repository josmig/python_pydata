import pandas as pd

## Un Dataframes es un conjunto de datos

tabla = pd.read_csv(r'/Users/miguelpantigoso/Downloads/datos.csv',sep=';', engine='python')
##print(tabla)
## Una serie es una lista de datos unidimensional cada columna y fila vendria a ser serie

##Skiprows es para poder ignorar las filas inciales si es que hay otro contenido
tabla = pd.read_csv('/Users/miguelpantigoso/Downloads/ventasTotales.csv', sep=';', skiprows=5)
#print(tabla)


#atributo shape[] : Devuelve el dato relacionado a la cantidad de filas y columnas de nuestro dataframe confirma las dimensiones 
# de nuestro dataframe

print(tabla.shape)
print(tabla.shape[0]) #podemos verlo por indices
print(tabla.shape[1]) 


#si queremos visualizar una cantidad especificas de filas
print(tabla.head(6))