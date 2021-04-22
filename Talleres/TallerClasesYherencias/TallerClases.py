# PUNTO 1

class Torta():
    '''
    Define la torta a tu gusto
    '''

    def __init__(self, forma, sabor, altura):
        self.forma = forma
        self.sabor = sabor
        self.altura = altura
    
    def mostrarAtributos (self):
        print('''mis atributos son:
        forma -->''', self.forma, '''
        sabor -->''', self.sabor, '''
        altura -->''', self.altura)

tortaChocolate = Torta("redonda", "Chocolate", "0.5m")
tortaChocolate.mostrarAtributos ()
torta1 = Torta("Circular", "milo", "1 metro")
torta1.mostrarAtributos ()

# PUNTO 2 

class Estudiante():
    def __init__(self, edad, nombre, id, carrera, semestre):
        self.edad = edad
        self.nombre = nombre
        self.id = id
        self.carrera = carrera 
        self.semestre = semestre
    
    def tiempoEstudio (self):
        '''
        Define una materia y el tiempo que la estudiarás, esto se mostrará en pantalla
        '''
        materiaEstudiar = str(input("¿Cuál materia estudiarás?: "))
        tiempoEstudiar = str(input("¿Cuánto tiempo la estudiarás?: "))
        print ("estudiarás la materia", materiaEstudiar, "por", tiempoEstudiar)

estudiante1 = Estudiante(19, "Jhon", "1000644865", "Ing. biomédica", "3er semestre")
estudiante1.tiempoEstudio()

# PUNTO 3

class Nutricionista ():
    def __init__ (self, edad, nombre, universidadEgresado):
        self.edad = edad
        self.nombre = nombre
        self.uni = universidadEgresado

    def IMC (self):
        peso = float(input("¿Cuánto pesas?: "))
        altura = float(input("¿Cuánto mides?: "))
        imc = peso/(altura**2)
        print ("Tu IMC es:", imc, "%")

nutricionista1 = Nutricionista(19, "Diego", "Universidad CES")
nutricionista1.IMC()

# PUNTO 4

class Canguro():
    def __init__(self, edad, id, nombre):
        self.edad = edad
        self.id = id
        self.nombre = nombre

    def saltos (self, saltos):
        for numero in range(saltos):
            print ("El canguro ha dado: ", saltos)

canguro1 = Canguro("9", "01", "Cangu")
canguro1.saltos (5)

