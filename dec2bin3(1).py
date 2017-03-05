def dec2bin3(s):
    ''' Input: A string s representing a
           positve decimal integer n 
       Output: The binary representation of n '''
     
    y = 0
    
    code = {'0' : 0b0, '1' : 0b1, '2' : 0b10, '3' : 0b11, 
                '4' : 0b100,  '5' : 0b101, '6' : 0b110,
                '7' : 0b111, '8' : 0b1000, '9' : 0b1001}    
    
    for ch in s[:]:
        w = code[ch]
        y = (y << 3) + (y << 1) + w
        
    data = []
    
    while y > 0:
        digit = y & 1
        data = [digit] + data
        y = y >> 1
        
    return data

        
    