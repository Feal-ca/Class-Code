from yogi import tokens


def cuadrat_curios(n: int) -> None:
    """
    Imprimeix per pantalla un 'cuadrat magic' de tamany n
    """
    n2 = n
    n3 = n - 1

    for i in range(n):
        print(i * str((n3 % 10)), end="")
        n3 = n3 - 1
        n2 = n - i
        for j in range(n - i):
            n2 = n2 - 1
            print(n2 % 10, end="")

        print("")


first = True
for a in tokens(int):
    if first:
        cuadrat_curios(a)
        first = False
    else:
        print("")
        cuadrat_curios(a)
