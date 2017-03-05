def selectK(S, k):    
    '''
    Input:  A list of numbers S, 
        a positive integer k
    Output: The k-th smallest element of S
    
    '''
    n = len(S)
    
    if k > n:
        return None
    
    from random import choice
    u = choice(S)
    
    SL = []; SD = []; SR = []
    
    for x in S:
        if x < u:
            SL = SL + [x]
        elif x == u:
            SD = SD + [x]
        else:
            SR = SR + [x]
            
    print(SL, u, SR)
    
    lenL = len(SL)
    lenR = len(SL) + len(SD)
    
    if k <= lenL:
        return selectK(SL, k);
    elif k <=lenR:
        return u
    else:
        k = k - lenR
        return selectK(SR, k);    
    

S = list(range(20))