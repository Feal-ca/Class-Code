def gcd_old(a,b):
    while b!=0:
        c=b
        b=a%b
        a=c
    return a

def gcd4(a,b,c,d):
    a1=gcd(a,b)
    a2=gcd(c,d)
    return gcd(a1,a2)

def gcd(a: int,b: int)-> int:
    if b == 0:
        return a
    c=b
    b=a%b
    a=c
    return gcd(a,b)

if __name__=="__main__":
    for a in range(10000):
        for b in range(10000):
            if gcd(a, b)!=gcd_old(a,b):
                print("HERE")
                print(a,b)