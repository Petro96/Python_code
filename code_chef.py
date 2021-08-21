##################################################################################
################################# Code chef ######################################
#### imports ###############


############################

### sum of digits

def f(n):
    s=0
    length = n
    arr=[]

    for i in range(length):
        num = input('input numbers')
        arr.append(num)

    for j in range(len(arr)):

        for k in range(len(arr[j])):

            s=s+int(arr[j][k])
        print(s)
        s=0

#f(3)

#### add two numbers

#solution 1
def f2(n):

    s=0
    for k in range(n):
        
        for i in range(2):
            num = int(input())

            s=s+num
        print(s)
        s=0

#f2(3)
        
#solution 2

def f3(n):
    s=0
    arr=[]

    for i in range(n):
        a=int(input('num1'))
        b=int(input('num2'))
        arr = arr + [a+b] # append()
    for num in arr:
        print(num)

#f3(3)
    
##### first and last

def f4(n):
    s=0
    arr=[]
    result = []
    for i in range(n):
        num = input('number ')
        arr.append(num)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            f= int(arr[i][0])
            l=int(arr[i][len(arr[i])-1])
        result.append(f+l)

    for num in result:
        print(num)

#f4(3)

#### factorial

def factorial(n):

    if n==1:
        return 1
    else:
        return n*factorial(n-1)

def f5(n):

    arr=[]
    result=[]

    for i in range(n):
        num = int(input('numbers '))
        arr.append(num)

    for num in arr:
        result.append(factorial(num))

    for j in range(len(result)):
        print(result[j])

#f5(3)

###  Turbo Sort

def f_sort(arr):

  return sorted(arr)

arr=[2,5,7,1,4,9]
#print(f_sort(arr))

#### Lucky four
def f6(n):
    s=0
    arr=[]

    for i in range(n):
        num = input('numb: ')
        arr.append(num)
    print(arr)
    for j in range(len(arr)):
        for k in range(len(arr[j])):
            if arr[j][k] == '4':
                
                s+=1
        print('sum od 4:',s)
        s=0
#f6(3)
    
#### REverse number
def f7(n):
    arr = []
    arr_reverse = []
    reverse =''
    for i in range(n):
        num = input('number: ')
        arr.append(num)

    for j in range(len(arr)):
        for k in range(len(arr[j])-1,-1,-1):
            reverse= reverse+arr[j][k]
        arr_reverse.append(reverse)
        reverse=''
        
    for num in arr_reverse:
        print(num)

#f7(3)

#### Seckond Largest   
        
def f8(m,n):

    arr = []
    arr_extern = []
    maximum = 0
    m_second = 0

    for i in range(m):
        for j in range(n):
            num = int(input('Number '))
            arr.append(num)
        arr_extern.append(arr)
        arr = []
        
    print(arr_extern)
    
    for k in range(len(arr_extern)):
        for l in range(len(arr_extern[k])):
            
            if arr_extern[k][l] > maximum:
                maximum = arr_extern[k][l]
                
                
        #print(maximum)
        arr_extern[k].remove(maximum)
        m_second = max(arr_extern[k])
        print('Second maximum,',m_second)
        m_second=0
        maximum =0

#f8(2,3)    

#### LEAD GAME -- >> game

### Chef and Operators 
def f9(n):

    arr = []
    arr_extern = []

    equal = '='
    greater = '>'
    less = '<'
    result = ''

    for i in range(n):
        for j in range(2):
            num = int(input('num '))
            arr_extern.append(num)
        arr.append(arr_extern)
        arr_extern = []
    print('Array of numbers : ',arr)
    for k in range(len(arr)):
        for n in range(len(arr[k])):
            if arr[k][0] == arr[k][1]:
                result += equal
            if arr[k][0] > arr[k][1]:
                result +=greater
            if arr[k][0] < arr[k][1]:
                result +=less
        
        print(result)
        result=''
                

#f9(3)
        
### Chef and Remissness

def f10(n):
    s = 0
    minimum = 0
    maximum = 0
    arr = []
    arr_extern = []

    for i in range(n):
        for j in range(2):
            num = int(input('num '))
            arr_extern.append(num)
        arr.append(arr_extern)
        arr_extern = []

    for k in range(len(arr)):
        for n in range(1):
            print('array ',arr)
            maximum = max(arr[k])
            minimum = min(arr[k])
            s = maximum + minimum
        print('min ',minimum,'s ',s)

        s=0
        minimum =0
        maximum=0

#f10(2)

### valid triangles

def valid_triangles(n):

    s = 0
    arr = []
    arr_extern = []

    for i in range(n):
        for j in range(3):
            
            num = int(input('angel in deegres'))
            arr_extern.append(num)

        arr.append(arr_extern)
        arr_extern = []
    print(arr)
    for k in range(len(arr)):
        for n in range(1):
            s=sum(arr[k])
          
        if s == 180:
            print('YES, its valid triangel.')
            s=0
        else:
            print('NO, its not valid triangel.')
            s=0
        
#valid_triangles(2)

#### Decrement or Increment

def d_or_i():
    result = 0
    while True:

        i =int( input('num '))

        if i == -1:
            break

        if i % 4 == 0:
            i+=1
            print(i)

        else:
            i -= 1
            print(i)

    print('End')

#d_or_i()

### prime numbers

### id and ship

def id_(n):

    arr = ['BattleShip','Cruiser','Destroyer','Frigale']

    for k in range(n):

        i = input('id ')

        if i == arr[k][0]:
            print(arr[k])

        if i.upper() == arr[k][0]:
            print(arr[k])

        else:
            print('Theres no ID . ')

#id_(2)

### puppy and sum

### total expenses
#total price * discount / 100 --> result - total price => 
def total(n):

    result = 0
    total_result = 0

    for i in range(n):
        for k in range(1):
            
            n = int(input('quantity :'))
            m =int(input('price : '))

            if n > 1000:
                result = (m * 10 )/100
                total_result = (m-result) *n
                print('Price with discount: ',total_result)

            else:
                total_result = m * n
                print('Price without discount: ',total_result)

#total(2)

### Grade the steel
                
def steel(n):

    print('1.Hardness > 50\n2.Carbon content < 0.7\nTensile strength > 5600 :')
    arr = []
    
    for i in range(n):
        for j in range(3):
            num = float(input('number : '))

            arr.append(num)
        if arr[0] > 50 and arr[1] < 0.7 and arr[2] > 5600 :
            print('10 --> all three condition are met.')
        elif arr[0] > 50 and arr[1] < 0.7 :
            print('9 --> (1) and (2) are met.')
        elif arr[1] < 0.7 and arr[2] > 5600 :
            print('8 --> (2) and (3) are met.')
        elif arr[0] > 50 and arr[2] > 5600 :
            print('7 --> (1) and (3) are met.')
        elif arr[0] > 50 or arr[1] < 0.7 or arr[2] > 5600:
            print('6 --> only one is met.' )
        else:
            print('5 --> none of three condition are met.')
        arr = []

#steel(2)

### greede puppy , you leaving coin for puppy 
# N M --> N - (M*M)

def puppy(n):

    result = 0

    for i in range(n):
        for j in range(1):

            num1 = int(input('number1: '))
            num2 = int(input('number2: '))

            result = num1 - (num2 * num2)

            print(result,'coins will leave for Tuzik. ')
        result = 0

#puppy(2)

### chef and fruits, you need to have equal apples and oranges,

def fruits(n):

    result  = 0
    r = 0

    for i in range(n):
        for j in range(1):

            a = int(input('apples: '))
            o = int(input('oranges '))
            c = int(input('coins'))

        if a == o:
            print('equal',result)

        if a > o and c > 0:
            r = a - o # 5 3 1
            if r == c:
                print(result,'equal')
            else:
                print(r,'difference')

        if o > a and c > 0:
            r = o - a
            if r == c :
                print(result,'equal')
            else:
                print(r,'difference')
#fruits(1)       
                
### vowel or consonant
def check(c):

    vowels = ['A','E','I','O','U']

    for i in range(len(vowels)):
        
        if vowels[i].upper() == c :
            
            print('Vowel')
        
    else:
        print('Consonant')

#check('e')

def how_many_digits(n):

    print('1 is one digit number\n2 is two digit number\n3 is three digit number\nmore than 3 if N more than three')
    length = 0
    for i in range(n):

        n = str(input('number: '))
        length = len(n)
        if length == 1:
            print('1')
        elif length == 2:
            print('2')
        elif length == 3:
            print('3')
        else:
            print('More than three digit')

#how_many_digits(4)

#### Minimum and Maxium          
def m(arr):

    maximum = 0

    for i in range(len(arr)):

        if arr[i] > maximum :
            maximum = arr[i]

    return maximum

#arr = [1,3,23,121,35,5]
#print(m(arr))

            

    
        
        



            
                    
                

            

        
    

        
            
    
    

        

    
    

    
            
        
        



        
        



