#CONSTANTES 
MAIN_MESSAGE = '''Choose an option introducing the corresponding number:
    1- You will get a conversion of the list from dollars to colombian pesos or euros
    2- program will show you the level of your monthly earnings.
    3- program wil show you: highest earning, lowest earning and an average of them
    4- finish program process.
    '''
CURRENCY_MESSAGE = '''Choose an option:
    C- to convert the list in colombian pesos
    D- for the current list (in dollars)
    E- to convert the list in euros
    '''
INVALID_MESSAGE = "invalid option"
PESOS_MESSAGE = "List in pesos : "
DOLARS_MESSAGE = "current dollar list: "
EUROS_MESSAGE = "List in euros : "
PERSON_EARN_QUESTION = "Introduce your monthly earning"



#Lists
DollarList = [20000, 30000, 4000, 2500, 1000, 7600]
PesosList = []
for numero in DollarList:
    conversion = round (numero*3700, 2) 
    PesosList.append (conversion)
EurosList = []
for numero in DollarList:
    conversion = round (numero*0.84, 2)
    EurosList.append (conversion)

ChosenOption = int(input(MAIN_MESSAGE))
while (ChosenOption != 4):
    print ("-----------------------")
    if (ChosenOption == 1):
        ListOption = str(input(CURRENCY_MESSAGE))
        if (ListOption == "C"):
            print (PESOS_MESSAGE, PesosList)
        elif (ListOption == "D"):
            print (DOLARS_MESSAGE, DollarList)
        elif (ListOption == "E"):
            print (EUROS_MESSAGE, EurosList)
        else:
            print ("invalid option")
        print ("----------------------------------")
    elif (ChosenOption == 2):
        print ("-----------------------------")
        ClassificationList = []
        for element in DollarList:
            if (element <= 1000):
                LowNumber = element
                print (LowNumber, "----> low income")
                ClassificationList.append (element)
            elif (element > 1000 and element <= 7000):
                MediumNumber = element
                print (MediumNumber, "----> Medium income")
                ClassificationList.append (element)
            elif (element > 7000 and element <= 20000):
                HighNumber = element
                print (HighNumber, "----> High income")
                ClassificationList.append (element)
            else:
                VeryHighNumber = element
                print (VeryHighNumber, "----> Very High income")
                ClassificationList.append (element)
        print(ClassificationList)
        print ("---------------------------------")
    elif (ChosenOption == 3):
        print ("----------------")
        isMax = max(DollarList)
        isMin = min(DollarList)
        isAverage = sum(DollarList)/len(DollarList)
        print ("The highest income is:", isMax)
        print ("The lowest income is:", isMin)
        print ("The average income is:", isAverage)
        print("---------------------------------------")
    else:
        print ("invalid option")
        print("-------------------------")
    ChosenOption = int(input(MAIN_MESSAGE))
print ("Thank you for use the program")

