#------función para línea divisora------#
def splitterline (symbol='-', quantity=10):
    print (symbol*quantity)
    return None

splitterline ('-', 30)

#---------muestre lista-------#
def showlist(list=[]):
    for elemento in list:
        print (elemento)
    return None

list1 = [215, 545, 248, 786, 526]
list2 = [21, 55, 48, 86, 26]

showlist (list1)
splitterline ('-', 10)
showlist (list2)
splitterline ('-', 10)

#---------sumar numeros-------#

def add(a=0, b=0):
    '''
        Devuelve la suma de dos números a y b
        sus valores predeterminados son cero
    '''
    sum = a + b
    return sum

result = add(12, 13)
print (result)
splitterline()

#---------restar numeros-------#

def substract(a=0, b=0):
    substraction = a - b
    return substraction

result = substract(12, 13)
print (result)
splitterline()

#---------multiplicar numeros-------#

def multiply(a=0, b=0):
    multiplication = a * b
    return multiplication

result = multiply(12, 13)
print (result)
splitterline()

#---------dividir numeros-------#

def divide(a=0, b=1):
    division = a/b
    return division

result = divide(12, 13)
print (result)
splitterline()

#-------tambien se puede acortar el paso del resultado poniendo la función en el print----#

print(divide(16,8))
splitterline()

#-----funciones dependientes de otras (e inputs)--------#

NumberA = int(input('Ingresa el número A: '))
NumberB = int(input('Ingresa el número B: '))

def calculate (operation, Anumber = 0, Bnumber = 0):
    print(operation(Anumber,Bnumber))

calculate(multiply, NumberA, NumberB)