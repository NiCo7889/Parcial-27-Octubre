"""
En este ejercicio se os pide crear un fichero llamado listasCEU.py que realice las siguientes funcionnes
Define una lista que contenga al menos 4 elementos de todos los tipos de valores permitidos en Python.
Selecciona cada dos elementos (uno si otro no) desde el final de la lista.
Cambia solamente la posición del primer elemento con el último elemento de la lista.
Elimina el último elemento de la lista modificada en el paso anterior.
Crea una nueva lista con la repetición de los elemento de la lista guardada en el paso anterior.
"""

lista = [1, "string", 3.4, True]
print(lista(-1, -3))
print(lista.pop(-1))
print(lista.remove(-3))

lista_repetida = [True, "string", 3.4]
print(lista_repetida.remove(-1))

lista_para_repetir = [True, "string", 3.4, True, "string", 3.4]
print(lista_para_repetir.count())
