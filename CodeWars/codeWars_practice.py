######################### CodeWars ##########################################


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

def array_diff(a,b):
    
    for i in range(len(a)):
        
        x = a[i]
        y = b[0]
        t = list(filter(lambda x:x!=y,a))
        
    return t

print(array_diff([1,2,2,2,3],[2]))


##  test = list(filter(lambda x: x != 26, test))
##  adults = filter(myFunc, ages)
##  for x in adults:
##  print(x)


arr = [2,3,34,26,75,26,1,26]
a = [2,3]

for i in range(len(arr)):
    x = arr[i]
    for j in range(len(a)):
        
        y = a[j]
        
        t = list(filter(lambda x:x!=y,arr))

#test = list(filter(lambda x: x != 26,arr))
#print(test)
print(t)





































