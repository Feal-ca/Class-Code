from yogi import tokens, read
from math import log

def es_creixent_decreixent(b: int, n: int,d: int):
    """
    Indica (True) si n en base b los digitos impares desde la izquierda son crecientes, y los pares decrecientes 
    """
    if d%2==0:
        if n<(b*b*b):
            if (n%b)<=(n//(b*b))%b:
                return False

            return True
        else:
            if (n%b)<=(n//(b*b))%b:
                return False
            if (n//b)%b>=(n//(b*b*b))%b:
                return False
            return es_creixent_decreixent(b, n//(b*b), d)
    else:
        if n<(b*b):
            return True
        else:
            if (n%b)>=(n//(b*b))%b:
                return False
            if (n//b)%b<=(n//(b*b*b))%b:
                return False
        
            return es_creixent_decreixent(b, n//(b*b), d)


if __name__ == "__main__":
    for b in tokens(int):
        n = read(int)
        if n==0: #:(
            print("YES")
        else:
            d = int(log(n,b))
            if es_creixent_decreixent(b,n,d):
                print("YES")
            else:
                print("NO")

#
