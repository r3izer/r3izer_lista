items = [] 
""" Declaramos una lista vacia que luego llenaremos con la funcion input() y append()"""

print("             LLENAR LISTA                 ")
"""Ingresamos un rango para la cantidad de elementos que contendra la lista"""

rango = int(input("Ingrese la cantidad de elementos : "))  

for i in range(rango):
    items.append(input("Añadir un elemento en la lista : "))
print("Elementos que se agregaron al llenar la lista : " +" "+str(items) )
"""Luego de agragar elementos se pueden hacer modificacines en la lista"""
"""  Agregamos una modificación a los elementos de la lista y los mostramos """

items[0] = "sword"
items[1] = "spear"
print("Nuevos elementos de la lista : " +" "+str(items))
