from yogi import read

def suma_digitos(n: int) -> int:
    """
    Devuelve la suma de los digitos de un entero positivo
    """ 
    sum = 0
    while (n != 0): 
        sum = sum + (n % 10)
        n = n//10
    return sum

def es_primer(n):
    if n==0 or n==1:
        return False
    i = 2
    while i*i<=n:
        if n%i == 0:
            return False
        i = i+1
    return True

def reduction_of_digits(n: int)->int:
    """
    Devuelve la suma reiterativa de los digitos de un numero
    """
    if n<10:
        return n
    return reduction_of_digits(suma_digitos(n))

def is_perfect_prime(n: int)-> bool:
    if not es_primer(n):
        return False
    if n<10:
        return True
    return is_perfect_prime(suma_digitos(n))

if __name__=="__main__":
    while True:
        n = read(int)
        print(is_perfect_prime(n))