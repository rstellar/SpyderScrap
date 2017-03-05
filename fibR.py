def  fibR(n):
    
    ''' input: A positve integer n 
       output: The fibonnacci number Fn 
       Recursive implementation'''
    
    if not isinstance(n, int) or n <= 0:
        return None  
    
    if n <= 2:
        return 1
    
    return fibR(n-1) + fibR(n-2)