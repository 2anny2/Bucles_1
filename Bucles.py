#Imprime todos los números enteros del 0 al 150.
for i in range(151):
    print(i)

#Imprime todos los multiplos de 5 entre 5 y 1000.
for i in range(5, 1001, 5):
    print(i)

#Contar a la manera del Dojo
for i in range(1, 151):
    if i % 10  == 0 and i % 5 == 0:
        print(i, "es multiplo de 10")
    elif i % 5 == 0:
        print(i, "es multiplo de 5") 
    else:
        print(i, "no es multiplo de 5 ni de 10")

#Whoa. Agrega los enteros impares del 0 al 500,000, e imprime la suma final.
suma = 0
contador = 0
for i in range(0, 500001):
    if i % 2 != 0:
        suma +=  i
        contador = contador + 1
print("El total de los numeros impares es: ", contador)
print("La suma de los numeros impares es: ", suma)

#Cuenta regresiva de a 4
for i in range(2018, -1, -4):
    print(i)

#Contador flexible. El bucle debe imprimir 3, 6, 9 (en líneas sucesivas). 
lowNum = 2
highNum = 9
mult = 3
for i in range(lowNum, highNum+1):
    if i % 3 == 0:
        print(i)
