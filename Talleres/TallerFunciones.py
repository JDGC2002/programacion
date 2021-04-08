def splitterline (symbol ='-', times = 15):
    print (symbol*times)
    return None

TestList = [52, 13, 46, 452, 456, 62, 23, 82, 35]

#POINT 1

def ShowListElementToElement (list1):
    '''
    this function will show in screen a list element to element
    '''
    number = 0
    for number in list1:
        print (number)
    return number

ShowListElementToElement(TestList)
splitterline()

#POINT 2

def ListMaxMinAvr (list1):
    '''
    this function will show you the highest/lowest number and an average of them
    '''
    print ("The highest number is:", max(list1)) 
    print ("The lowest number is:", min(list1))
    print ("The lowest number is:", sum(list1)/len(list1))
    return None

ListMaxMinAvr(TestList)
splitterline()

#POINT 3

def Greetings (times, Message):
    messagetimes = times*(
    '''
    
    '''+ Message)
    print (messagetimes)
    return messagetimes

Greetings(5, "He aquí una hoguera, deberías descansar.")
splitterline()

#POINT 4 

def EvenNumbers (list1):
    for number in list1:
        if (number%2 == 0):
            print (number)
    return None

EvenNumbers(TestList)
splitterline()

#POINT 5

def NumbersHigerThan24 (list1):
    for number in list1:
        if (number>24):
            print(number)
    return None

NumbersHigerThan24 (TestList)
splitterline()

#POINT 6 

def IMCcalculator (weight, height):
    IMC = weight/(height*height)
    print (IMC)
    return IMC

IMCcalculator (90, 1.75)
splitterline ()

#POINT 7

def FarwellMessage (Message):
    print (Message)
    return None

FarwellMessage ("La re buena pa' todos")
splitterline ()







