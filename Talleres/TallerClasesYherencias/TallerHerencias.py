#Punto 1

class Persona ():
    def __init__(self, id, nombre, edad):
        self.id = id
        self.nombre = nombre
        self.edad = edad
    
    def Hablar (self, mensaje):
        ''' 
        escribe un mensaje que desees que la persona diga
        '''
        print (mensaje)
    
    def Caminar (self, distancia):
        '''
        muestra en pantalla cuanto ha caminado según la distancia que introduzcas en Km
        '''
        print ("he recorrido", distancia, "Km")

# PUNTO 2

class Doctor (Persona):
    def __init__ (self, id, nombre, edad, especialidad):
        Persona.__init__(self, id, nombre, edad)
        self.especialidad = especialidad

    def Curar (self, enfermedad):
        nombre = self.nombre
        print ("Hola, soy el Doctor", nombre, "y procederé a curar la enfermedad", enfermedad)

doctor1 = Doctor(1, "Diego", 19, "neurología")
doctor1.Curar ("Alzheimer")

#PUNTO 3

class Nutricionista (Persona):
    def __init__(self, id, nombre, edad, universidadEgresado):
        Persona.__init__(self, id, nombre, edad)
        self.universidadEgresado = universidadEgresado

    def IMC (self):
        peso = float(input("¿Cuánto pesas?: "))
        altura = float(input("¿Cuánto mides?: "))
        imc = peso/(altura**2)
        print ("Tu IMC es:", imc, "%")

nutricionista1 = Nutricionista(2, "Pablo", 35, "CES")
nutricionista1.IMC()

#PUNTO 4 

class Abogado (Persona):
    def __init__(self, id, nombre, edad, especialidad, universidadEgresado):
        Persona.__init__(self, id, nombre, edad)
        self.especialidad = especialidad
        self.universidadEgresado = universidadEgresado

    def Trabajar (self, nombreRepresentado, caso):
        nombre = self.nombre
        print ("Soy el abogado", nombre, ". Procederé a representar al cliente", nombreRepresentado, "en el caso de", caso)

abogado1 = Abogado(3, "Alberto", 55, "protección a ladrones", "CES")
abogado1.Trabajar ("Álvaro Uribe Vélez", "falsos positivos")
