#classes are user defined blueprint or prototype
#sum, multiplication, addition, constant
#classes have methods, class variables, instance variables, constructor etc.

#objects for your classes-

#===========================#
#Self keyword is mandatory for calling variable names into method
#instance and class variables have whole different purpose
#constructor name should be __init__
#new keyword is not required when you create object


class Calculator:
    num = 100 #class variables
    #default constructor

    def __init__(self,a,b):
        self.firstNumber= a
        self.secondNumber= b
        print("I am called automatically when object is created")


    def getData(self):
        print("I am now executing as a method in class")

    def Summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num


obj = Calculator(2,3) #syntax to create objects in python
obj.getData()
print(obj.Summation())

obj1 = Calculator(4,5) #syntax to create objects in python
obj1.getData()
print(obj1.Summation())

