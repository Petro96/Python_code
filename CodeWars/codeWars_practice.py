######################### CodeWars ##########################################

import random

# import for Kivy

# from re import MULTILINE
# from kivy.app import App
# from kivy.uix.label import Label
# from kivy.uix.widget import Widget
# from kivy.lang import Builder
# from kivy.animation import Animation
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.textinput import TextInput
# from kivy.uix.button import Button
# from kivy.properties import ObjectProperty
# from kivy.core.window import Window






#A Narcissistic Number is a positive number which is the sum of its own digits,
#each raised to the power of the number of digits in a given base.
#In this Kata, we will restrict ourselves to decimal (base 10).

# 153, len('153')=3 =>>> 1**3 + 5**3 + 3**3 = 153 ---> 153==153 => True


def narcissistic( value ):
    # Code away
    str_num = str(value)
    number_len=(len(str_num))
    sum_of_digits = 0
    for i in range(number_len):
        sum_of_digits += (int(str_num[i]))**number_len
        
    if sum_of_digits == value:
        return True
    return False

#print(narcissistic(153))
#print(narcissistic(1938))

# Your task is to write a function maskify, which changes all but the
# last four characters into '#'.


def maskify(cc):
    
    if cc == '' or len(cc)<=4:
        
        return cc
        
    elif len(cc)>=4:
        
        str_len=(len(cc))-4
        arr=list(cc)
        
        for i in range(str_len):
            arr[i]='#'
        
        return "".join(arr)
    
    

s = 'Skippy'
#print(maskify(s))

def maskify(cc):
    return "#"*(len(cc)-4) + cc[-4:] # [start:end]

#print(maskify("123456789"))




# In this little assignment you are given a string of space separated numbers,
# and have to return the highest and lowest number.

def high_and_low(numbers):
    
    n_list = list(numbers)
    max_num = int(n_list[0])
    min_num = int(n_list[0])

    for i in range(len(n_list)):

        if int(n_list[i])>max_num:
            max_num = int(n_list[i])

        if int(n_list[i])<min_num:
            min_num = int(n_list[i])

    
    
    return "".join(str(max_num)+","+str(min_num))

numbers = "1 2 3 4 5"
"".join(numbers)
n_list = list(numbers)
#print(n_list)
#print(numbers)


#print(high_and_low("12345"))  # return "5 1" --> works without white spaces 
##high_and_low("1 2 -3 4 5") # return "5 -3"
##high_and_low("1 9 3 4 -5") # return "9 -5"


#If a name has exactly 4 letters in it, you can be sure that it has to be
#a friend of yours! Otherwise, you can be sure he's not...

#Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]


def friend(x):
    #Code
    arr=[]
    for item in x:
        if len(item)==4:    
            arr.append(item)
    return arr

friends = ["Ryan","Kieran","Mark"]
#print(friend(friends))

def friend(x):
    return list(filter(lambda s : len(s)==4 ,x))
#print(friend(friends))



# example of exercise : accum("abcd") -> "A-Bb-Ccc-Dddd"
#                       accum("cwAt") -> "C-Ww-Aaa-Tttt"

def accum1(s):
    
    string = ''
    new =''
    
    
    for i in range(len(s)):
        
        for j in range(i+1):
        
            if j==0:
                
                string+=s[i].upper()
                
                
            elif j>0:
                
                string += s[i].lower()
                
        if i<len(s)-1:
            string+="-"
                
    return string

#print(accum1('abcde'))
#print(accum1('cwAt'))

def accum2(s):
    output = ""
    for i in range(len(s)):
        output+=(s[i]*(i+1))+"-"
    return output.title()[:-1]

#title() -> return string with upper capital word

#print(accum2('abcde'))
#print(accum2('cwAt'))


# It should remove all values from list a, which are present in list b
# keeping their order.

# array_diff([1,2],[1]) == [2]
# array_diff([1,2,2,2,3],[2]) == [1,3]

def array_diff(a, b):
    #your code here
   
    if len(a)==0:
        return a
    elif len(b)==0:
        return a
    elif len(a)>0 and len(b)>0:
        f=a
        for i in range(len(b)):
            f = list(filter(lambda x:x!=b[i],f))
    return f
        

##print(array_diff([1,2,2],[2]))
##print(array_diff([1,2,2],[]))
##print(array_diff([],[2]))
##print(array_diff([1,2,2,3,4,3,3],[2,3,4]))

def array_diff(a, b):
    return [x for x in a if x not in b]


##  test = list(filter(lambda x: x != 26, test))
##  adults = filter(myFunc, ages)
##  for x in adults:
##  print(x)


#If we list all the natural numbers below 10 that are multiples of 3 or 5,
#we get 3, 5, 6 and 9. The sum of these multiples is 23.

#Finish the solution so that it returns the sum of all the multiples of 3 or 5
#below the number passed in. Additionally, if the number is negative, return 0
#(for languages that do have them).

#Note: If the number is a multiple of both 3 and 5, only count it once.
# (15 -> multiplay with 3 and 5)
# number = 1000 ==>> 233168

def solution(number):
    
    arr=[]
    sum_of = 0

    for i in range(number):

        if i%3==0 or i%5==0:
            arr.append(i)
            sum_of+=i

    return sum_of,arr

#print(solution(1000))

#Given: an array containing hashes of names

#Return: a string formatted as a list of names separated
#by commas except for the last two names, which should be separated
#by an ampersand

#namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

##arr = [{'name':'Mary'}]
##
##for item in arr:
##    for k in item:
##        print("NAME:",item['name'])

def namelist(names):
    #your code here
    s = ''
    if len(names)==0:
        return s
    elif len(names)==1:
        s+=names[0]['name']
        return s
    elif len(names)>1:
        for i in range(len(names)):
            
            s+=names[i]['name'] # dict {'name':"Brand"}
            if i<len(names)-2:
                s+=", "
            else:
                s+=" & "
    return s[:-3] # -3 ->> because of white space at the end !!! 'Bert '
            
#names = [ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ]
#names = [ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'},{'name': 'John'},{'name': 'Lucy'} ]
names = [{'name':'Mosh'},{'name':'Molly'}]
#names = [{'name':'Mery'}]
#names = []
#print(namelist(names))

#Given n, take the sum of the digits of n. If that value has more than one digit,
#continue reducing in this way until a single-digit number is produced.
#The input will be a non-negative integer.

def digital_root(number):

    while number > 9:

        number = sum(int(x) for x in str(number))
        
    return number
        

#print(digital_root(12345))



def f(number):

    while number > 9: # I need to stop summing when my number has one digit

        number = sum(int(x) for x in str(number))

    return number

#print(f(12345)) # 1+2+3+4+5 = 15 > 1+5 = 6(digit root number)


# Define a function that takes one integer argument and returns logical value
# true or false depending on if the integer is a prime.


def is_prime(n):

    if n <=1:
        return 0
    else:
        for i in range(2,n):

            if n%i==0:
                return False
        else:
            return True

#print(is_prime(42))  # --->>> is to slow (12000 ms


def prime_finder(n):
  # Write your code here
  arr=[]
  for i in range(n+1):
    if prime_number(i):
      arr.append(i)
  return arr

def prime_number(number):
  if number<=1:
    return 0
  else:

    for i in range(2,number):
      if number%i==0:
        return False
    return True

    
 
#print(prime_finder(11))


def sum_char(s):
    
    
    
    sum_of=0
    for item in s:
        
        for item2 in s:
            
            if item==item2:
                
                sum_of+=1
        
        if sum_of>1:
            
            return False
        sum_of=0
        
    return True

#print(sum_char("apple"))


def unique_characters(string_in):
  if string_in=="":
    print("String is empty")
  else:
 
    sum_of=0
    for item in string_in:
      for item2 in string_in:
        if item==item2:
          sum_of+=1
      if sum_of>1:
        return False
      sum_of=0
    return True
 
 
#print(unique_characters("apple"))

        
# Write a function that takes in a string of one or more words, and
# returns the same string, but with all five or more letter words reversed

# spinWords( "Hey fellow warriors" )   =>  returns "Hey wollef sroirraw"
# spinWords( "This is a test")         =>  returns "This is a test"
# spinWords( "This is another test" )  =>  returns "This is rehtona test"


def spinWords(sentence):

    pass
    
    
        

def reverse_word(sentence):
    

    arr = sentence.split()
    
    if sentence == "":
        
        return 0
    
    return "".join(arr[0][::-1])





#print(reverse_word("Hello World"))
    
word = "Hello World"
#spinWords(word)
#print(word)


# products of everything else
# For example, product_of_the_others([1, 2, 3, 4, 5])
# should return [120, 60, 40, 30, 24]

def product_of(arr):

    product = 1
    arr_of_products = [] 

    for i in range(len(arr)):

        for j in range(len(arr)):
            
            if arr[j]!=arr[i] :

                product*=arr[j]
                
        arr_of_products.append(product)
                
        product=1

    return arr_of_products

        

#arr = [1,2,3,4,5]
arr = [5,5,5]

print(product_of(arr))


    
        
    



    

    
































