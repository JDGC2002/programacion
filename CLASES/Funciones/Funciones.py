#Existe algo llamado return, eso significa que la función devuelve algo modificado, en caso de que solo devuelve lo que se le indicó, será return none
#un ejemplo de return none sería print, pues solo muestra lo que se le indicó
#un ejemplo de return algo, sería round, el cual hace un proceso de redondeo y devuelve una modificación
#ponemos return none por buena práctica.

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

#---------multiplicar numeros-------#

def divide(a=0, b=1):
    division = a/b
    return division

result = divide(12, 13)
print (result)
splitterline()









































































