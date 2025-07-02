

## Una lista nos permite almacenar en la memoria del ordenador varios valores no como una simple variable
myLista=["Maria","pepe","Lucho","Antonio"]

print(myLista[:]) # asi se imprime una lista
print(myLista[3]) #imprimir segun el indice
print(myLista[0:3]) #con esto debe accedera los 3 primeros elementos

print(myLista[:2]) #con esto accedes a los dos ultimos elementos

#para agregar un nuevo elemento a la lista (al final)
myLista.append("Miguel")

#para agregar en cualquier lugar
myLista.insert(2, "Rosa")

print(myLista[:])


#podemos concatenar con otras listas
myLista.extend(["Sandra","Wendy","Paola"])
print(myLista[:])


#para saber el indice de un elemento
#print(myLista.index("Naara"))

#si este elemento se encuentra en mi lista
print("Jose" in myLista)

#para eliminar yltimo valor 
myLista.pop()
print(myLista[:])




