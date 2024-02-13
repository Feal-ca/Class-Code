# se me olvida quitar los prints :(

from math import sqrt
def sum_divisors(n):
    sum = 0
    i = 1
    while i*i < n:
        if n%i==0:
            sum = sum+i+(n//i)
        i = i+1    
    if sqrt(n)%1==0:
        sum = sum +sqrt(n)
    return(int(sum)) 
