from yogi import read


def escriure(L: list[int]) -> None:
    print("("+",".join([str(x) for x in L])+")")


def generar_permutacions(n: int, words: list[str]) -> None:
    """
    Escriu totes les permutacions d'n zeros i uns, per a n ≥ 0.
    """

    generar_permutacions_rec(
        n, ["" for _ in range(n)], words, 0, [False for _ in range(n+1)])


def generar_permutacions_rec(n: int, L: list[int], words: list[str], i: int, used: list[bool]) -> None:
    """Escriu totes les permutacions d'n zeros i uns
    que comencin amb L[:i], amb |L| = n ≥ i ≥ 0."""

    if i == n:
        escriure(L)
    else:
        for num in range(n):
            if not used[num]:
                used[num] = True
                L[i] = words[num]
                generar_permutacions_rec(n, L, words, i+1, used)
                used[num] = False


def main() -> None:
    n = read(int)
    words = [read(str) for _ in range(n)]
    generar_permutacions(n, words)


if __name__ == "__main__":
    main()
