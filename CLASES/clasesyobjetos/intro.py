class Human():
    def __init__(self, nameIntroduce, oldIntroduce, heightIntroduce):
        print("Hello, I'm a new human.")
        self.oldness = oldIntroduce
        self.race = "Human"
        self.name = nameIntroduce
        self.height = heightIntroduce

    def ShowAtributtes (self):
        print ("My name is ", self.name, ". I'm", self.oldness, "y/o", ". my height is", self.height, "Mts")
    
    def speak (self, message):
        print ("I have a message for you: ", message)

    def savings (self):
        '''
        Human will save amount of money you introduce
        '''
        saveQuestion = int(input('''Introduce
        1 --> if you want to save an amount of money
        2 --> if you do not want to save money
        '''))
        if (saveQuestion == 1):
            amountQuestion = float(input("Introduce an amount of money that human will save: ")) 
            print ("I will save", amountQuestion)
        elif (saveQuestion == 2): 
            print ("Ok")
        else:
            print ("non valid option")


class biomedic (Human):
    def biomedicalEquipmentMaintenance (self, EquipmentName):
        print ("Hi, I am", self.name, "and I will give the appropiate mantenance to", EquipmentName)

bioHuman = biomedic("Diego", 19, 1.75)
bioHuman.biomedicalEquipmentMaintenance ("Electrocardiogram")



human1 = Human("Diego", 18, 1.75)
human1.ShowAtributtes ()
human1.savings ()
human1.speak("Espero que estés muy bien")

human2 = Human("Kaiser", 9, 1.00)
human2.speak("Hasta luego")


