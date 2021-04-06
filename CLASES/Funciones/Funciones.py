#------función para línea divisora------#
def splitterline (symbol='-', quantity=20):
    print (symbol*quantity)
    return None


#---------muestre lista-------#
def showlist(list=[]):
    for elemento in list:
        print (elemento)
    return None


#---------sumar numeros-------#

def add (a=0, b=0):
    '''
        Devuelve la suma de dos números a y b. 
        sus valores predeterminados son cero
    '''
    addition = a + b
    return addition




#---------restar numeros-------#

def substract(a=0, b=0):
    substraction = a - b
    return substraction

result = substract(12, 13)


#---------multiplicar numeros-------#

def multiply(a=0, b=0):
    multiplication = a * b
    return multiplication

result = multiply(12, 13)


#---------dividir numeros-------#

def divide(a=0, b=1):
    division = a/b
    return division

result = divide(12, 13)

#-----funciones dependientes de otras (e inputs)--------#


def calculate (operation, Anumber = 0, Bnumber = 0):
    print(operation(Anumber,Bnumber))



