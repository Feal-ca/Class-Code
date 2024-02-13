from yogi import tokens, read


def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False
    return primes


def es_primer(n, primes):
    return primes[n]


def composite():
    """
    Retorna el primer numero compost d'una llista, o 'no' si no n'hi ha cap
    """
    last = read(str)
    primes_limit = 10**8  # adjust this limit based on your input constraints
    primes = sieve_of_eratosthenes(primes_limit)

    for num in tokens(str):
        if not es_primer(int(last + num), primes):
            return last + num
        last = num

    return "no"


print(composite())
