#funcion Map
lista = [28,45,67,8,92,10,3,6,32,77]
print(list(map((lambda valor: valor * valor), lista)))
#(en el ejemplo de arriba se consiguió el cuadrado de cada uno de los elementos de la lista)

#funcion Filter
print(list(filter((lambda valor: valor%2==0),lista)))

#funcion Reduce
import functools
print(str(functools.reduce((lambda x,resultado:x+resultado),lista)))
