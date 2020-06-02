import random
import math

def miller_rabin(n, a):
    d = 1
    dd = 1
    k = int(math.log2(n-1))+1 
    for i in range(k, -1, -1):
        d = (d*d) % n
        if d == 1 and dd != 1 and dd != n-1:
            return False
       
        b_i = ((n-1) >> i) & 1
        if b_i:
            d = (d * a) % n
        
        dd = d

    return d == 1

print(miller_rabin(65, 8))
print(miller_rabin(65, 12))
