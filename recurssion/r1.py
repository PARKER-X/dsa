# Factorial of a number
def factorial(n):
    if n==0:
        return 1
    else:
        return n* factorial(n-1)
# print(factorial(5))

# fibnoacci number
def fib(n) :
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
# print(fib(6))

# Powerset
def powerset(s):
    x = len(s)
    for i in range(1<<x):
        c=[]
        for j in range(x):
            if i &(1<<j):
                c.append(s[j])
        print(c)
# print(powerset([1,2,3]))

def powerset2(s):
    lists = [[]]
    for i in range(len(s)+1):
        for j in range(i):
            lists.append(s[j:i])
    return lists 
print(powerset2([1,2,3]))


