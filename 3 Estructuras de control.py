#!/usr/bin/python3

# 3.1 Condicionales (if)

print("\nif condicion_1 :")
print("\tbloque de codigo")
print("elif condicion_2 :")
print("\tbloque de codigo")
print("...")
print("else :")
print("\tbloque de codigo\n")

edad = 14
if edad <= 18 :
    print("Menor")
elif edad > 65 :
    print("Jubilado")
else :
    print("Activo")

age = 20
if age <= 18 :
    print("Menor")
elif age > 65 :
    print("Jubilado")
else :
    print("Activo")

# 3.2 Bucles condicionales (while)

print("\nwhile condicion :")
print("\tbloque de codigo\n")

# Pregunta al usuario por un numero hasta que introduce 0
num = None
while num != 0 :
    num = int(input("Introduce un numero : "))
# Pregunta al usuario por un numero hasta que introduce 0
while True :
    num = int(input("Introduce un numero : "))
    if num == 0 :
        break