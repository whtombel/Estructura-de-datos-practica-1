import random

lista = [13,14,15,16,18,19,21,22,24,25,28,30,31,33,34,36,39,40,42,43]


#colocar la lista en orden aleatorio
random.shuffle(lista)
print (lista)

#organizar la lista
lista.sort()
print (lista)

#encuentra la posicion
posicion = lista.index(16)


print ("la edad 16 años si existe y esta en la posicion", posicion)
print ("el tamaño de la lista es ",len(lista))


