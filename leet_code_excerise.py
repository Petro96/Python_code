#################################################################################
########################### Data Structure - Arrays #############################

import random


## 

arr=[1,2,0,5,6,7,0,1]

#my solution - that I try :)

'''
print('My solution')
arr2=[1,0,3,0,4,0,5]
i=0
length=len(arr2)
while i<length:
    
    if arr2[i]==0:
        arr2.insert(i+1,0)
        arr2.pop()
        i+=2
    else:
        i+=1
       
print(arr2)
'''

# examples #####################################################

## ex1
'''
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        
        zeroCount = 0
        for a in arr:
            if a == 0:
                zeroCount += 1
                
        if zeroCount == 0:
            return
        
        n = len(arr)
        input = len(arr) - 1
        output = input + zeroCount
        
        while input >= 0:
            if arr[input] == 0:
                if output < n:
                     arr[output] = 0
                output -= 1
            if output < n:
                arr[output] = arr[input]
            output -= 1
            input -= 1
 '''           
#ex2
'''
class Solution:
    def duplicateZeros(self, arr) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        arr2 = []
        for i in range(len(arr)):
            arr2.append(arr[i])
            if arr[i] == 0:
                arr2.append(0)
        #print(arr2)
        arr[:] = arr2[:len(arr)] # do arr da prvke s arr2 velkosti arr
        #arr=arr2  # it cant be,because of length of array
'''
#print('Array without modification ',arr)
#print('Solution 1')
#Solution().duplicateZeros(arr)
#print(arr)

#print('list:',arr[:])
#arr2=[12,3,5,6,7,0]
#print(arr2[:len(arr)])
#arr=arr2
#print(arr)

#ex3 its not correct
'''
class Solution:
    def duplicateZeros(self, arr) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i=0
        l=len(arr)
        while i < l:
            if arr[i]==0:
                arr.insert(i+1,0) #i+1
                arr.pop()
                i+=2
            else:
                i+=1
#print('Solution 2')
#Solution().duplicateZeros(arr)
#print(arr)
'''



################# Merge Sorted

## examples

#nums1 , nums2 ,m ,n -> nums1=length(m+n->0),result(m+n numbers)
# merge to the nums1

def input_data():
    m=int(input('m='))
    n=int(input('n='))
    return m,n

#print(data[0])
#print(data[1])

def make_nums2(n):
    
    nums2=[]
    for i in range(n):
        nums2.append(random.randint(1,15))
    return nums2

def make_nums1(m,n):
    
    nums1=[]
    for i in range(m):
        nums1.append(random.randint(1,26))
    for j in range(n):
        nums1.append(0)
    return nums1

#print(make_nums1(data[0],data[1]))
#print(make_nums2(data[1]))


class Solution(object):
    def merge(self, nums1, m, nums2, n):

        for i in range(n): #len(nums1)-m
            nums1.pop()
        for j in range(n): #0,n
            nums1.append(nums2[j])
        nums1.sort()

def main():
    data=input_data()

    array1=make_nums1(data[0],data[1])
    array2=make_nums2(data[1])

    print('Arrays:')
    print(array1)
    print(array2)

    Solution().merge(array1,data[0],array2,data[1])
    print(array1)
    
#main() 

######## Deleting elements

#Input: nums = [0,1,2,2,3,0,4,2], val = 2 remove element val
#Output: 5, nums = [0,1,4,0,3,_,_,_]

#exercise 2 duplicates remove
    
#Input: nums = [0,0,1,1,1,2,2,3,3,4]
#Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]


# 1

class Solution(object):
    def removeElement(self, nums, val):

        i=0
        end=len(nums)
        while i<end:
            
            if nums[i] == val:
                #print(nums[i])
                #del nums[i]
                nums.remove(nums[i])
                end-=1
                
            else:
                i+=1
            
                
        length=len(nums)

        return length


arr=[1,23,4,3,5,6,4,9,4]

#print(Solution().removeElement(arr,4))

#del arr[2]
#arr.pop(1)
#arr.remove(4) #just one 4

#print(arr)

#2
arr_doubles=[1,1,1,2,2,3,3,4,5,5]

class Solution(object):
    def removeDoubles(self, nums):
        
        counter=0
        i=0
        length=len(nums)-1

        while i < length:

            if nums[i] == nums[i+1]:
                counter+=1

            if counter >= 1:
                nums.remove(nums[i])
                length-=1
                counter=0
            else:
                i+=1
        return len(nums)   
        

#print('Doubles remove')
#print(arr_doubles)
#print(Solution().removeDoubles(arr_doubles))
#print(arr_doubles)

#############################################################################
## Searching items in an array

## ex1

#Given an array arr of integers, check if there exists two integers N and M
#such that N is the double of M ( i.e. N = 2 * M).
#More formally check if there exists two indices i and j such that :

    #i != j
    #0 <= i, j < arr.length
    #arr[i] == 2 * arr[j]

# i -> search for result , j -> search for numb N=2*M

numbers = [4,2,10,3,7,5]
'''
class Solution(object):
    def checkIfExist(self, arr):
        counter=0

        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[i] == 2*arr[j]:
                    counter+=1

        return counter
 '''   
#print(Solution().checkIfExist(numbers))

#primer 2
    
class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        zero_count = 0 # To count the zeros
        for num in arr:
            if num != 0 and num * 2 in arr: #  check for mulipication by 2 
                return True
            elif num == 0 :
                zero_count += 1
        
        return True if zero_count > 1 else False
#print(Solution().checkIfExist(numbers))

#example 2
'''
a = [3,1,7,11]
class Solution:
    def checkIfExist(self, arr):
        for num in arr:
            if num==0 and arr.count(num)>1:
                return True
            elif num!=0 and (num/2 in arr or num*2 in arr):
                return True
        return False
print(Solution().checkIfExist(a))
'''
#ex2
#iven an array of integers arr, return true if and only if it is a valid mountain
#array.
#Recall that arr is a mountain array if and only if:

    #arr.length >= 3

#arr=[0,2,3,2,1]   #True
#arr=[3,5,5]        #False
#arr=[0,2,3,3,5,2,1] #False

#class Solution(object):
 #   def validMounten(self, arr):

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        i = arr.index(max(arr))
        if i == 0 or i == len(arr)-1:
            return False
        j = 1
        while j < len(arr)-1:
            if (j <= i and arr[j] <= arr[j-1]) or (j >= i and arr[j] <= arr[j+1]):
                return False
            j += 1
        return True







