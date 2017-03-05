def divide(x, y):
    ''' Input: Two n-bit integers x and y, 
           where y >= 1 
       Output: The quotient and remainder of x
           divided by y'''

    
    if x == 0:
        return [0, 0]
    
    bits = dec2bin(x)
    
    q = 0; r = 0
    
    for digit in bits:
        q = 2*q; r = 2*r
        r = r + digit
        if r >= y:
            q = q + 1; r = r - y
    
    
    return [q, r]
    
    
    
def dec2bin(n):
    ''' Input: A positve decimal integer n 
       Output: The binary representation of n '''
    
    data = []
    
    while n > 0:
        digit = n & 1
        data = [digit] + data
        n = n >> 1
        
    return data