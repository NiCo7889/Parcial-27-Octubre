"""
Crea un Script llamado recorrido.py que realice las siguientes funciones:

Recorre el listado del ejemplo y realiza las siguientes operaciones: [18, 50, 210, 80, 145, 333, 70, 30]

Imprimr el número en caso de que sea múltiplo de 10 y menor que 200
Parar el programa si llega a un número mayor que 300
"""
numeros = [18, 50, 210, 80, 145, 333, 70, 30]

for num in range(0,7):   
    if num%10==0 and num<200:
        num1=input("Introduce un numero:")
        print(f"Este numero {num1} es múltiplo de 10 y menor que 200 ")
