class Humano ():
    def __init__(self, nombre, sexo, edad):
        self.nombre = nombre
        self.sexo = sexo
        self.edad = edad
    
    def Hablar (self, mensaje):
        ''' 
        escribe un mensaje que desees que el humano diga
        '''
        print (mensaje)

class Doctor (Humano):
    def __init__ (self, nombre, sexo, edad):
        Humano.__init__(self, nombre, sexo, edad)

    def IMC (self):
        peso = float(input("¿Cuánto pesas?: "))
        altura = float(input("¿Cuánto mides?: "))
        imc = peso/(altura**2)
        print (f'Tu IMC es de {imc} %')

doctor1 = Doctor('Jhon', 'Hombre', 30)
doctor1.IMC()
