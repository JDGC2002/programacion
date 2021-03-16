#CONSTANTES 
MAIN_MESSAGE = '''Choose an option introducing the corresponding number:
    1- You will get a conversion of the list from celsius to farenheit or kelvin.
    2- program will show you the level of your temperature.
    3- program will show you: highest temperature, lowest temperature 
    and how many hours go from take a temperature to other.
    4- finish program process.
    '''
CURRENCY_MESSAGE = '''Choose an option:
    F- to convert the list in Fahrenheit temperature.
    K- to convert the list in Kelvin temperature.
    C- current celsius list.
    '''
INVALID_MESSAGE = "invalid option"
FAHRENHEIT_MESSAGE = "List in Fahrenheit: "
CELSIUS_MESSAGE = "current celsius list then it is not necessary to convert: "
KELVIN_MESSAGE = "List in Kelvin: "
PERSON_EARN_QUESTION = "Introduce your monthly earning"



#Lists
CelsiusList = [36,37,38,35,36,38,37.5,38.2,41,37.4,38.6,39.1,40.3,33]
KelvinList = []
for number in CelsiusList:
    conversion = round (number+273.15, 2) 
    KelvinList.append (conversion)
FahrenheitList = []
for numero in CelsiusList:
    conversion = round (numero*1.8+32, 2)
    FahrenheitList.append (conversion)

ChosenOption = int(input(MAIN_MESSAGE))
while (ChosenOption != 4):
    print ("-----------------------")
    if (ChosenOption == 1):
        ListOption = str(input(CURRENCY_MESSAGE))
        if (ListOption == "F"):
            print (FAHRENHEIT_MESSAGE, FahrenheitList)
        elif (ListOption == "K"):
            print (KELVIN_MESSAGE, KelvinList)
        elif (ListOption == "C"):
            print (CELSIUS_MESSAGE, CelsiusList)
        else:
            print ("invalid option")
        print ("----------------------------------")
    elif (ChosenOption == 2):
        print ("-----------------------------")
        ClassificationList = []
        for element in CelsiusList:
            if (element < 36):
                hypothermia = element
                print (hypothermia, "----> Your current temperature level is: Hypothermia")
                ClassificationList.append ("Hypothermia")
            elif (element >= 36 and element <= 37.6):
                Normal = element
                print (Normal, "----> Your current temperature level is: regular")
                ClassificationList.append ("Regular")
            else:
                Fever = element
                print (Fever, "----> Your current temperature level is: Fever")
                ClassificationList.append ("Fever")
        print(ClassificationList)
        print ("---------------------------------")
    elif (ChosenOption == 3):
        print ("----------------")
        isMax = max(CelsiusList)
        isMin = min(CelsiusList)
        isAverage = round (len(CelsiusList)/24, 1)
        print ("The highest temperature is:", isMax)
        print ("The lowest temperature is:", isMin)
        print ("Each temperature were taken each:", isAverage, "hours")
        print("---------------------------------------")
    else:
        print ("invalid option")
        print("-------------------------")
    ChosenOption = int(input(MAIN_MESSAGE))
print ("Thank you for use the program")
