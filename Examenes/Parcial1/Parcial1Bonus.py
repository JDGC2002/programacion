import Parcial1 as p 

Value1 = float(input("Introduce value1: "))
Value2 = float(input("Introduce value2: "))
Value3 = float(input("Introduce value3: "))

TestList1 = [91, 52, 64, 32, 82, 91]
TestList2 = [56, 21, 67, 82, 13, 45]
TestList3 = [45, 12, 96, 17, 56, 37]

#POINT 1
p.SumSubsMult(Value1, Value2, Value3)
print ("-"*15)

#POINT 2
p.ShowThreeList (TestList1, TestList2, TestList3)
print ("-"*15)

#POINT 3
base = float(input("introduce the area of the triangle: "))
alture = float(input("introduce the height of the triangle: "))

p.AreaCalculator(base, alture)
print ("-"*15)

#POINT 4
p.ListMaxMinAvr (TestList1)
print ("-"*15)

#POINT 5
ValueFi = int(input("Introduce for fibonacci serie: "))
p.FibSer (ValueFi)
print ("-"*15)
