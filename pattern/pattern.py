# Prime Number
def prime(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                return "Non-Prime"
            else:
                return 'Prime'
    return "Non-Prime"
print(prime(13))

