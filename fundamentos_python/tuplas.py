#listas inmutables donde no se puede a;adir elementos ni eliminar menos mover (no append,extend y remove)
#No permiten busquedas (no index)
#Si permiten si un elemento se encuentra de una tupla comprobar

##Y cual es su utilidad ? mas rapida , menos espacio, formatean strings y pueden utilizar como claes en un diccionario
myTupla= ('jUAN',123,321,2,3)
miLista = list(myTupla)
print(miLista)
print(myTupla)

#Convertir lista en tupla
miList=['Juan','Valladres',123,321,123]
mitupla=tuple(miList)
print(mitupla.count(123)) #para contar
print(len(mitupla)) #para ver la longitud de la tupla
tupla=('hola',) #tupla unitaria