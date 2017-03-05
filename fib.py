def fib(n):
    ''' input: A positve integer n 
       output: The fibonnacci number Fn '''
    
    if not isinstance(n, int) or n <= 0:
        return None   
    
    data = [1]*n
    
    for k in range(2, n):
        data[k] = data[k-1] + data[k-2]
        
    return data[-1]