from yogi import read

def es_primer(n):
    if n==0 or n==1:
        return False
    i = 2
    while i*i<=n:
        if n%i == 0:
            return False
        i = i+1
    return True

def suma_digitos(n: int) -> int:
    """
    Devuelve la suma de los digitos de un entero positivo
    """ 
    sum = 0
    while (n != 0): 
        sum = sum + (n % 10)
        n = n//10
    return sum

def is_perfect_prime(n: int)-> bool:
    if n>=10:
        return is_perfect_prime(suma_digitos(n)) and is_palindromic(n) and es_primer(n)

    if not es_primer(n):
        return False
    return True

def is_palindromic(a):
    a=str(a)
    if int(a) != int(a[::-1]):
        return False
    else:
        return True

if __name__=="__main__":
    n = 1
    while True:
        if is_perfect_prime(n) and is_palindromic(n): print(n)
        n = n + 1

