print ('#########')
for i in range (10):
    print(i)
print ('#########')

for i in range (10):
    print(i+1)
print ('#########')

for i in range (1,11):
    print (i)
print ('#########')

for i in range (1,11,2):
    print (i)
print ('#########')

for i in range (1,10):
    if (i%2 == 0):
        print (i)
print ('#########')

for i in range (1,10):
    if (i%2 != 0):
        print (i)
print ('#########')

for i in range (1,11):
    if (i%2 == 0):
        print (i, '-->Número par')
    else:
        print (i, '--> Número impar')
print ('#########')

#Ahora es usando inputs

rango = int(input("Seleccione el rango máximo: "))
opcion = int (input('''
    1- Ver solo pares
    2- Ver solo impares
    3- Ver todos
    N- Ver nada
    '''))

if  (opcion == 1):
    for i in range (1, rango+1):
        if (i%2 == 0):
            print (i)
elif (opcion == 2):
    for i in range (1, rango+1):
        if (i%2 != 0):
            print (i)
elif (opcion == 3):
    for i in range (1, rango+1):
        print (i)
else:
    print ('mostrando nada...')



