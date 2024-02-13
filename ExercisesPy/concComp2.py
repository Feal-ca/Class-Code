from yogi import tokens, read
from math import sqrt

def es_primer(n: int) -> bool:
    """
        Retorna si un numero es primer (True) o no (False)   
    """
    if n==0 or n==1:
        return False
    
    b = int(sqrt(n))+1
    for a in range(2,b):
        if n%a == 0:
            return False
    return True


n1 = read(str)
no = True

for n2 in tokens(str):
    num = (n1+n2)
    n1 = n2
    if not es_primer(int(num)):
        print(num)
        no = False
        break

if no:
    print("no")
