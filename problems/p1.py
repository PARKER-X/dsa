# Reverse the integer 123-->321
def reverse_integer():
    n = (input("Num: "))
    return n[::-1]

# print(reverse_integer())

# complement of base 10 integer python
def bitwiseComplement():
    N= int(input("Num"))
    s = str(bin(N))
    sum = 0
    num = 1
    for i in s[::-1]:
        if i == "b":
            return sum
        elif i =="0":
            sum+=num
        num*=2

# print(bitwiseComplement())

# Power of two
def Power_of_two():
    n = int(input("Num:"))
    if n<0:
        return False
    while (n!=1):
        if (n%2!=0):
            return False
        n = n//2
    return True
# print(Power_of_two())

array = [1,2,3,4,5,6,7,8]
def array_sway(arr):
    n=1
    c=[]
    d=[]
    while n< len(arr):
        c.append(arr[n])
        
        n-=1
        c.append(arr[n])
       
        n+=3
        c.append(arr)
    for i in c:
        c = str(i)
        print(c)
        if len(c)==1:
            d.append(c)


    return d

# print(array_sway(array))

import numpy as np

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

r = np.fliplr(x.reshape(3,-1)).flatten()

# print(list(r))
        



#Find unique element in array 
array1=[1,1,2,2,3,4,4]
def findUnique(arr) :
    ans=0
    for i in range(len(arr)):
        ans=ans^arr[i]
    return ans
        

# print(findUnique(array1))

# unique no. of occurence  
array2 = [1,1,2,3,3,2,2,4,4,4,4]
def unique(arr):
    c=[]
    d = list(set(arr))
    for i in range(len(d)):
        c.append(arr.count(d[i]))
    return True if len(c)==len(set(c)) else False



# print(unique(array2))


# Give the duplicate element in array
arr1 = [1,2,3,4,5,2,4]
def duplicate(arr):
    arr.sort()
    arr1 =[]
    arr2 =[-1]
    n = len(arr)
    for i in range(n-1):
        if arr[i]==arr[i+1]:
            arr1+=[arr[i]]
    arr1= [*set(arr1)]
    
    arr1.sort()
    if len(arr1)>=1:
        return arr1
    else:
        return arr2



# print(duplicate(arr1))


#Intersection b/w two sorted arrays
arr11 = [2,3,4,5,9]
arr22 = [2,3,4,5,6,7,9]
def intersection(arr11, arr22):
    c=[]
    for i in arr11:
        if i in arr22:
            c.append(i)
    return c

# print(intersection(arr11, arr22))

# Two arr sum
from collections import defaultdict
arr10=[2,1,3,4,6,7]
def two_sum(arr, sum):
    s = defaultdict(int)
    cnt = 0
    for ele in arr:
        if sum-ele in s:
            cnt += s[sum-ele]
        s[ele] += 1
    return cnt
            
            
    

# print(two_sum(arr10,10))

# Triplet sum in an array
A= [1,2,3,7,6]
def find3Numbers(A, n, X):
        for i in range(n-1):
            s = set()
            
            for j in range(i+1, n):
                if X - (A[i] + A[j]) in s:
                    return True
                s.add(A[j])
        
        return False

print(find3Numbers(A, 5,10))




   

 

    

