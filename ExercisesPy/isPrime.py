from math import sqrt
def es_primer(n):
    if n==0 or n==1:
        return False
    b = int(sqrt(n))+1
    for a in range(2,b):
        if n%a == 0:
            return False
    return True
