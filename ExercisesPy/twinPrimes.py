from yogi import tokens


def are_primes(m: int, n: int) -> bool:
    """
    Indica si un parell de numeros que difereixen en 2 (m, n) son primers bessons, o no
    """
    i = 2
    while i*i <= max(m,n): # en aquest codi es sempre (n), pero podria no ser el cas 
        if n%i==0 or m%i==0:
            return False
        i = i+1
    return True


def nth_twin_primes(n: int) -> tuple[int, int]:
    """
    Returna una tuple amb la n-esima parella de numeros primers bessons
    """
    x = 1
    while n > 0:
        x = x+2
        
        if are_primes(x, x+2):
            n = n-1
        
    
    return (x,x+2)

if __name__ == "__main__":
    for n in tokens(int):
        a, b = nth_twin_primes(n)
        print(a,b)
