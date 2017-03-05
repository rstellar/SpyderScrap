def mergesort(x):
# input: a list of numbers x
# output: the sorted version of x

    n = len(x)
    if n <= 1:
        return x
    
    mid = n // 2
    left = x[0 : mid]
    right = x[mid : n]
    sorted_left = mergesort(left)
    sorted_right = mergesort(right)
    merged_list  = merge(sorted_left, sorted_right)
    return merged_list


# helper function

def merge(x, y):
# input: sorted lists of numbers x and y
# output: the sorted merger of x and y
 
    n = len(x) + len(y)
    z = [0] * n
    
    i = j = 0
    while i < len(x) and j < len(y):
        if x[i] <= y[j]:
            z[i+j] = x[i]
            i = i + 1
        else:
            z[i+j] = y[j]
            j = j + 1
            
          
    # loop invariant: 
    # i + j has increased by 1
    # 0 < i + j < len(x) + len(y)
    # loop has run i + j times     
     
    if i == len(x):
        z[len(x)+j :] = y[j :]
    else:
        z[i+len(y) :] = x[i :]
        
    return z

# Test input

w = [7, 8, 5, 9, 4, 2]
