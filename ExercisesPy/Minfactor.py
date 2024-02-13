from math import sqrt
def factor_mes_petit(n):
    for a in range(2,int(sqrt(n))+1):
        if n%a == 0:
            return a
    return None
"""while True:
    a = int(input())
    print(factor_mes_petit(a))"""