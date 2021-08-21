
import datetime
import math

class Exercise:
    counter=0
    def  __init__(self,a,b):
        self.a = a
        self.b = b
        #counting()
    def __repr__(self):
        return f'sides({self.a,self.b})'
    
    def pitagor_theory(self):
        c= math.sqrt((self.a**2)+(self.b**2))
        
        return c

    @classmethod
    def counting(cls): # cls -> __init__ : a,b
        return cls(['pythagor theory'],['fdcd'])
    
#ex=Exercise(5,2)
#print(round(ex.pitagor_theory(),2))

'''       
for i in range(10):
    ex=Exercise(i+1,2)
    print(round(ex.pitagor_theory(),2))
    #print(Exercise.counting())
   
e=Exercise.counting()
print(e)
'''

# in place array
'''
class Inplace:

    def f(self,arr):
        for i in range(len(arr)):

            if i % 2 ==0:
                arr[i]=arr[i]**2


def f(arr):

    for i in range(len(arr)):

        if i % 2 ==0:
            arr[i]=arr[i]**2
            
print('Squared numbers on the even indexes.')
print('Orginal ',arr)
arr=[9,2,3,5,6]

Inplace().f(arr)
print('Class solution ',arr)
f(arr)
print('modify ',arr)
'''

# classmethods , staticmethods

class Person(object):
    population = 50

    def __init__(self,name,age):

        self.name = name
        self.age = age
        
    @classmethod
    def getPopulation(cls):
        return cls.population

    @staticmethod
    def isAdult(age):
        return age >= 18

    def display(self):
        print(self.name, 'is', self.age, 'years old.')

newPerson = Person('John', 18)

#print(Person.getPopulation())
#print('age',newPerson.age)
#print(Person.isAdult(15))   #newPerson.age

# Inheritance

class Employee:

    raise_amt = 1.04
    num_of_emp = 0

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@gmail.com'
        self.pay = pay

        Employee.num_of_emp += 1

    def __repr__(self):
        return "Employee('{}','{}','{}')".format(self.first,self.last,self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(),self.email)

    #__str__ = __repr__

    def __add__(self,other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())
    
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls,emp_str):
        first ,last,pay = emp_str.split('-')
        return cls(first,last,pay) # object Employee
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() ==6:
            return False
        else:
            return True
        
    
    #@property
    #def email(self):
    #    return '{}.{}@gmail.com'.format(self.first,self.last)
    
    #@property --> than you can call fullname method like atribute not like func
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    #@fullname.setter
    #def fullname(self,name):
     #   first,last = name.split(' ')
      #  self.first = first
       # self.last = last

    #@fullname.deleter
    #def fullname(self,name):
        # print('Delet Name!')
         #self.first = None
         #self.last = None
       
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt) #Employee.raise_amt 

class Developer(Employee):

    raise_amt = 1.10 # class atribute
    
    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang = prog_lang
        
class Manager(Employee):

    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self,emp):

        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('--> ',emp.fullname())

    
dev_1 = Employee('John','Cortney',2000)
dev_2 = Employee('Anet','Silver',4000)
dev_3 = Developer('Shon','Kent',5000,'Python')
dev_4 = Developer('Michael','Sleev',3400,'PHP')
############################################
############################################


  

'''
print(dev_1.fullname())
print(dev_1.email)
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

print('\n ')

print(dev_3.fullname())
print(dev_3.email)
print(dev_3.prog_lang)
print(dev_3.pay)
dev_3.apply_raise()
print(dev_3.pay)
'''
'''
mgr_1 = Manager('Sue','Smith','9000',[dev_1])

print('Manager mail ',mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.add_emp(dev_4)

print('Employees that are managed: ')
mgr_1.print_emps()

print(isinstance(mgr_1,Manager))
'''
## Dunder Method

## repr  , str
print(dev_1.__repr__())
print(dev_1.__str__())

## add
print(int.__add__(1,2)) 
print(dev_1 + dev_2)

## len
print(len(dev_1))


### Property Decorators - setters,getters,deletters


#dev_1.first = 'Mark'
#print(dev_1.first)
#print(dev_1.email)

#dev_1.fullname('John Spenser')
#print(dev_1.email)

### Class Variables
#class atribute
#instance atribute 

print(dev_1.__dict__)
print('Number of employees:',Employee.num_of_emp)

## Classmethods , Staticmethods (constructors)

#classmethod
print('\nRaise Amount')
print(dev_1.raise_amt)
dev_1.set_raise_amt(1.05)
print(dev_1.raise_amt)

d= datetime.date(2021,7,24)
print(Employee.is_workday(d))


dev_5 = Employee.from_string('Joy-Firland-2100')
print(dev_5)
