# Decimal to Binary
def decimal_to_binary(n):
    
    if n>=1:
        decimal_to_binary(n//2)
        
    print(n%2, end='')

# print(decimal_to_binary(34))

def binary_to_decimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    print(decimal)   
     
        
        
        
    
    
print(binary_to_decimal(1010))



        