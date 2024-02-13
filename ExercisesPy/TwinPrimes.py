from yogi import tokens

def son_primers(n: int, m: int)->bool:
    """
    Indica (True) si tant n com m son primers, per n,m>=2.
    """

    i = 2
    while i*i<=max(n,m):
        if n%i == 0 or m%i==0:
            return False
        i = i+1
    return True

def nth_twin_primes(n: int)->tuple[int,int]:
    """
    Retorna l'n-esim parell de nombres bessons per a n>=1
    """
    x = 1
    i = 0
    while i<n:
        x = x+2
        if son_primers(x,x+2):
            i = i+1
    return (x,x+2)

if __name__ == "__main__":
    for n in tokens(int):
        print(nth_twin_primes(n))
