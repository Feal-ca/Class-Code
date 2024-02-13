from yogi import read


def escriure(L: list[int]) -> None:
    print(" ".join([str(x) for x in L]))


def generar_combinacions(n: int, o: int) -> None:
    """
    Escriu totes les combinacions d'n zeros i uns, per a n ≥ 0.
    """

    generar_combinacions_rec(n, [-1 for _ in range(n)], 0, o, 0)


def generar_combinacions_rec(n: int, L: list[int], i: int, o: int, ones: int) -> None:
    """
    Escriu totes les combinacions d'n zeros i uns que comencin amb L[:i], amb |L| = n ≥ i ≥ 0.
    """

    if i == n:
        escriure(L)
    else:
        if i-ones < n-o:
            L[i] = 0
            generar_combinacions_rec(n, L, i + 1, o, ones)
        if ones < o:
            L[i] = 1
            generar_combinacions_rec(n, L, i + 1, o, ones+1)


def main() -> None:
    n = read(int)
    o = read(int)
    generar_combinacions(n, o)


if __name__ == "__main__":
    main()
