############### OOP ######################################################

### Inheritance
### Polymorphism
### Encapsulation
### Abstraction

################# Inheritance ############################################
'''
class Dog(object):
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.li = [1,3,4]

    def speak(self):
        print("Hi I am", self.name, "and I am", self.age, "years old.")

    def change_age(self,age):
        self.age = age

    def add_weight(self,weight):
        self.weight = weight

    def talk(self):
        print("Bark")

class Cat(Dog):    ### if iam not use super()method ---> WET principle(DRY)
    
    def __init__(self,name,age,color):
       super().__init__(name,age)
       self.color = color
       
    def talk(self):
        
        print("Meow")

    

#-----------------------------------------------#   

c1= Cat("Maya",4,'black')
c1.speak()
c1.talk()

d1 = Dog("Tim",55)
d2 = Dog("Fred",3)

d1.change_age(5)
d1.add_weight(70)

d1.speak()
d1.talk()

d2.speak()
d2.talk()
'''

################################################################

##class Employee:
##
##    raise_amt = 1.04 #class variable(attribute)
##
##    def __init__(self,first,last,pay):
##        self.first = first  #instance variable,attribute
##        self.last = last
##        self.email = first + "."+last+'@gmail.com'
##        self.pay = pay
##
##    def fullname(self):
##        return '{} {}'.format(self.first,self.last)
##
##    def apply_rise(self):
##        self.pay = int(self.pay * self.raise_amt)
##
##class Developer(Employee):
##
##    raise_amt = 1.10
##    
##    def __init__(self,first,last,pay,prog_lang):  # help() method
##        super().__init__(first,last,pay)
##        self.prog_lang = prog_lang
##
##class Manager(Employee):
##
##    def __init__(self,first,last,pay,employees=None):
##        super().__init__(first,last,pay)
##        if employees is None:
##            self.employees = []
##        else:
##            self.employees = employees
##
##    def add_emp(self,emp):
##        if emp not in self.employees:
##            self.employees.append(emp)
##
##    def remove_emp(self,emp):
##        if emp in self.employees:
##            self.employees.remove(emp)
##
##    def print_emp(self):
##        for emp in self.employees:
##            print("-->",emp.fullname())


#----------------------------------------------------------#
'''
dev1 = Developer("Corey","Schafer",50000,"Pyhton")
dev2 = Developer("Jack","Moon",60000,"SQL")

manager1 = Manager("John","Simpson",45000,[dev1])

print(manager1.email)


manager1.add_emp(dev2)
manager1.print_emp()

#isinstance (is obj instance of class)
print(isinstance(manager1,Employee))

#issubclass
print(issubclass(Developer,Employee))
print(issubclass(Developer,Manager))

#print(help(Developer))

#print(dev1.pay)
#print(dev1.prog_lang)
#dev1.apply_rise()
#print(dev1.pay)
'''
### __name__ == '__main__' #########################################

# module from file
#import module

#print "First module name:{}".foramt(__name__)

def main():
    print("Run Directly!")

if __name__ == '__main__': #direcly by python
    main()
else:
    print("Run import!")  # import in another file

## try,except,finally,raise ##################################################

##try: 
##    f = open("test.txt")
##except: 
##    print('Could not open file')
##finally:
##    f.close()
##print('Program continue')

    
##raise ImportError # create error

################################# Abstract Classes ##########################

# -- allownes of data

from abc import ABC,abstractmethod

class Shape(ABC): # inherits in ABC(abstract) module
    
    @abstractmethod
    def area(self):pass

    @abstractmethod
    def perimeter(self):pass

class Square(Shape):
    
    def __init__(self,side):
        self.__side = side

    def area(self):
        return self.__side * self.__side

    def perimeter(self):
        return 4*self.__side

#shape = Shape() # error(abstractmethod)
square = Square(5) # error (inherit from abstractmethod)

##if __name__ == '__main__':
##    print("Im here , in this file.")
##    print(square.area())
##    print(square.perimeter())

  
class R(ABC):

    @abstractmethod
    def rk(self): 
        print("Abstract Base Class")
        
    @abstractmethod
    def print():
        print("hello")
  
class K(R):

    
    def rk(self): 
        super().rk() 
        print("subclass ")

    def print():
        print("hello World")

##r = K() 
##r.rk() 

########################## Classmethods, Staticmethods ######################
#Classmethod
        
# - methods(self)
# - classmethods(cls)
# - making changes inside class(class variables)
import datetime

class Employee:

    raise_amt = 1.04 #class variable(attribute)
    num_of_emps = 0

    def __init__(self,first,last,pay):
        self.first = first  #instance variable,attribute
        self.last = last
        self.email = first + "."+last+'@gmail.com'
        self.pay = pay

        Employee.num_of_emps +=1

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_rise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls,emp_str):
        first,last,pay = emp_str.split('-')
        return cls(first,last,pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday()==6:
            return False
        return True
        

emp1 = Employee("Corey","Schafer",50000)
emp2 = Employee("Jack","Moon",60000)

##print(emp1.fullname())
##print(emp2.fullname())
##
##Employee.set_raise_amt(1.05) #Employee.raise_amt = 1.05 / emp1.set_raise_amt(1.05)
##
##print(Employee.raise_amt)
##print(emp1.raise_amt)
##print(emp2.raise_amt)

## example of classmethod useage -- >>>  Alternative Constructor <<<< -------

emp_str1 = 'John-Deep-4500'
emp_str2 = 'Steve-Smith-5000'
emp_str3 = 'Jane-Doe-6000'

#first,last,pay = emp_str1.split('-')

#new_emp1 = Employee(first,last,pay)
new_emp1 = Employee.from_string(emp_str1)

#print(new_emp1.email)

## Staticmethod
# like regular functions

##my_date = datetime.date(2021,10,12)
##print(Employee.is_workday(my_date))

############

class Dog(object):

    dogs = []

    def __init__(self,name):
        self.name = name
        self.dogs.append(self)

    @classmethod
    def num_of_Dogs(cls):
        return len(cls.dogs)

    @staticmethod
    def bark(n):
        for i in range(n):
            print("BARK!")

d1 = Dog("Jacky")
d2 = Dog("Bobi")

print(Dog.num_of_Dogs())
print(Dog.bark(5))

################################## Property, setters,getters,deleters ##############



    


























