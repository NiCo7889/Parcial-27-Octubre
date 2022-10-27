"""
*Convertir la variable "var_1" en todas las letras mayúsculas y en minúsculas (var_1 = "Módulo 1 de Python ")

*Consulta el tamaño o la longitud de la variable "var_1" y calcula la división de ese numero entre "7" redondeado a 4 decimales

*Realiza una función llamada funcion1  que calcule siguiente operación para que el resultado final sea igual a cero (0) //12 - (4 * 2) - (2 + 2)
*Realiza una función llamada funcion2 para que calcule la siguiente operación para que el resultado final sea igual a catorce (14)// 12 - 4 * (2 - 2) + 2
*Realiza una función llamda funcion3 para pedir al usuario que introduzca su edad, y después imprimir en la pantalla si es meyor de edad o no
"""
var_1 ="Módulo 1 de Python "
print(var_1.upper())
print(var_1.lower())
num=len(var_1)
operacion=num/7
print(round(operacion,4))

def funcion1():
    op=12-(4*2)-(2+2)
    return op

print(funcion1())

def funcion2():
    op=12 - 4 * (2 - 2) + 2
    return op

print(funcion2())

def funcion3():
    edad=int(input("Inttroduce tu edad: "))
    if edad<18:
        print("Eres menor de edad.")
    else:
        print("Eres mayor de edad.")
print(funcion3())