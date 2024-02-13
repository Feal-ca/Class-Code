from yogi import read, tokens
from math import sqrt

def print_ordered_divisors(n: int) -> None:
    """
    Mostra per pantalla tots els divisors d'un enter (n) en ordre ascendent
    """
    print(f"divisors of {n}:",end="")
    a = int(sqrt(n))
    for i in range(1,a+1):
        if n%i==0:
            print(f" {i}",end = "")
    PerfSquare = int(a == sqrt(n))
    for i in range(PerfSquare,a):
        if n%(a-i)==0:
            print(f" {n//(a-i)}", end = "")
    print()

if __name__ == "__main__":
    for num in tokens(int):
       print_ordered_divisors(num)
