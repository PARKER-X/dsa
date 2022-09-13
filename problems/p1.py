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

def Power_of_two():
    n = int(input("Num:"))
    if n<0:
        return False
    while (n!=1):
        if (n%2!=0):
            return False
        n = n//2
    return True
print(Power_of_two())
