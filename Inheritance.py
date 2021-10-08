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

class Employee:

    raise_amt = 1.04 #class variable(attribute)

    def __init__(self,first,last,pay):
        self.first = first  #instance variable,attribute
        self.last = last
        self.email = first + "."+last+'@gmail.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_rise(self):
        self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):

    raise_amt = 1.10
    
    def __init__(self,first,last,pay,prog_lang):  # help() method
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

    def print_emp(self):
        for emp in self.employees:
            print("-->",emp.fullname())


#----------------------------------------------------------#

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



########################## Classmethods, Staticmethods ######################




























