from math import sqrt

def primer(n):
    if n==0 or n==1:
        return False
    for a in range(2,int(sqrt(n))+1):
        if n%a == 0:
            return False
    return True

def semiprimalitat(a: int)-> tuple[int, int] | None:
    for b in range(2,int((a/2))+1):
        if a%b==0:
            #print(b)
            a = a/b
            if es_primer(b) and es_primer(a):
                return (f"({b}, {int(a)})")
            else:   
                return None

if __name__=="__main__":
    pass
