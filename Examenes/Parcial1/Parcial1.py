#POINT 1

def SumSubsMult (Value1=0, Value2=0, Value3=0):
    '''
    This function will add, substract, multiplicate and divide the 3 values between them
    '''
    Sum = Value1+Value2+Value3
    Subs = Value1-Value2-Value3
    Mult = Value1*Value2*Value3
    Div = Value1/Value2/Value3
    Pot = Value1**Value2**Value3
    print ("add is =", Sum, ",", "substract is =", Subs, ",", "multiplication is =", Mult, ",", "divition is =", Div, ",", "potentiation is =", Pot)
    return Sum, Subs, Mult, Div, Pot

#POINT 2

def ShowThreeList (list1, list2, list3):
    '''
    Introduce 3 lists with the same lenght and program will show you them in screen
    if you introduce a shorter or longer list it won't be show
    '''
    if (len(list1) == len(list2) == len(list3)):
        print ('''

        ''',
        list1,
        '''

        ''',
        list2,
        '''

        ''',
        list3)
    else:
        print("There is a shorter or longer list")
    return list1, list2, list3

#POINT 3

def AreaCalculator (base= 0, alture= 0):
    '''
    This function will calculate the area of a triangle
    '''
    area = (base*alture)/2
    print (area)
    return area

#POINT 4

def ListMaxMinAvr (list1):
    '''
    this function will show you the highest/lowest number and an average of them
    '''
    print ("The highest number is:", max(list1)) 
    print ("The lowest number is:", min(list1))
    print ("The average is = ", sum(list1)/len(list1))
    return None

#POINT 5

def FibSer (Number):
    '''
    this function will show you the number before a number you choose in fibonacci serie
    '''
    if (Number==0):
        print (1)
    elif (Number==1):
        print (1)
    else:
        print ((Number-1)+(Number-2))












