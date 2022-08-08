#!/usr/bin/python3

# 2.1 Tipos de datos primitivos

# Numbers
numbers = 0 , -1 , 3 , 1415
print(numbers)
# Cadenas
strings = "Esta es una cadena" , 'Este es un typo de dato str'
print(strings)
# Booleanos
booleans = True , False
print(booleans)

# 2.2 Tipos de datos primitivos compuestos (contenedores)

# Listas
lists = [1 , "DOS" , [3,4] , True]
print(lists)
# Tuplas
tuples = (1 , 'dos' , 3)
print(tuples)
# Diccionarios
dictionaries = {"pi" : 3.1416 , 'e' : 2.718}
print(dictionaries)

# 2.3 Clase de un dato (type())

print(type(1))
print(type("Hello"))
print(type([1 , "dos" , [3 , 4] , True]))
print(type({"pi" : 3.1415 , 'e' : 2.718}))
print(type((1 , "DOS" , 3)))

# 2.4 Numeros (clases int y float)

print(type(1))
print(type(-2))
print(type(2.3))

# 2.4.1 Operadores aritmeticos

print(2 + 3)
print(5 * -2)
print(5 / 2)
print(5 // 2)
print(5 % 2)
print((2 + 3) ** 2)

# 2.4.2 Operadores logicos con numeros

print(3 == 3)
print(5 > 2)
print(5 < 2)
print(3.1 <= 3)
print(3.1 >= 3)
print(-1 != 1)

# 2.5 Cadenas (clase str)

print('Python')
print("123")
# Cadena Vacia  
print('')
# Cadena con un espacio en blanco
print(" ")
# Cambio de linea
print('\n')
# Tabulador
print("\t")

# 2.5.1 Acceso a los elementos de una cadena

print("-----------------------------------")
print("|Cadena         |P |y |t |h |o |n |")
print("|---------------------------------|")
print("|Indice Positivo|0 |1 |2 |3 |4 |5 |")
print("|---------------------------------|")
print("|Indice Negativo|-6|-5|-4|-3|-2|-1|")
print("-----------------------------------")

print("Python"[0])
print("Python"[1])
print("Python"[-1])
# print("Python"[6])

# 2.5.2 Subcadenas

print("Python"[1:4])
print("Python"[1:1])
print("Python"[2:])
print("Python"[:-2])
print("Python"[:])
print("Python"[0:6:2])

# 2.5.3 Operaciones con cadenas

print('Me gusta ' + 'Python')
print('Python' * 3)
print('y' in 'Python')
print('to' not in 'Python')

# 2.5.4 Operaciones de comparacion de cadenas

print("Python" == "python")
print("Python" < "python")
print("a" > "z")
print("A" >= "z")
print("" < "Python")

# 2.5.5 Funciones de cadenas

print(len("Python"))
print(min("Python"))
print(max("Python"))
print("Python".upper())
print('A,B,C'.split(','))
print("I love Python".split())

# 2.5.6 Cadena formateadas(format())

print("Un {} vale {} {}".format("€" , 1.12 , "$"))
print("Un {2} vale {1} {0}".format("€" , 1.12 , "$"))
print("Un {moneda1} vale {cambio} {moneda2}".format(moneda1 = "€" , cambio = 1.12 , moneda2 = "$"))
print("Hoy es {:^10}, mañana {:10} y pasado {:>10}".format("lunes" , "martes" , "miercoles"))
print("Cantidad {:5d}".format(12))
print("Pi vale {:8.4f}".format(3.141592))

# 2.6 Datos logicos o booleanos (clase bool)

print(True == 1)
print(False == 0)

# 2.6.1 Operaciones con valores logicos

print("==")
print(">")
print("<")
print(">=")
print("<=")
print("!=")
print("not b")
print("b1 and b2")
print("b1 or b2")

# 2.6.2 Tabla de verdad

print("----------------------------------")
print("|  x  |  y  |not x|x and y|x or y|")
print("|--------------------------------|")
print("|False|False|True | False |False |")
print("|--------------------------------|")
print("|False|True |True | False |True  |")
print("|--------------------------------|")
print("|True |False|False| False |True  |")
print("|--------------------------------|")
print("|True |True |False| True  |True  |")
print("----------------------------------")

print(not True)
print(False or True)
print(True and False)
print(True and True)

# 2.7 Conversion de datos primitivos simples

print(int("12"))
print(int(True))
print(float("3.14"))
print(float(True))
print(str(3.14))
print(str(True))
print(bool('0'))
print(bool('3.14'))
print(bool(''))
print(bool("Hello"))

# 2.8 Variables

lenguaje = "Python"
x = 3.14
y = 3 + 2
# Asignacion Multiple
a1 , a2 = 1 , 2
# Intercambio de valores
a , b = 1 , 2
a , b = b , a
# Incremento (equivale a x = x + 2)
x += 2
# Decremento (equivale a x = x - 1)
x -= 1
# Valor no definido
x = None
del x

# 2.9 Entrada por terminal (input())

language = input("¿Cual es tu lenguaje favorito ? ")
print(language)
age = input("¿Cual es tu edad ? ")
print(age)

# 2.9.1 Salida por terminal (print())

print("print(dato1 , ... , sep="" , end='\n' , file=sys.stdout)")

print("Hello")
name = "Leonardo"
print("Hello" , name)
print("El valor de pi es" , 3.1415)
print("Hello" , name , sep="")
print("Hello" , name , end="!\n")