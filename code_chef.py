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

#### REverse number

#### Seckond Largest

    





        
        



