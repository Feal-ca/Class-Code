from typing import Optional


def average(s: set[float]) -> float:
    """
    Retorna el valor mitja d'un set de floats (s)
    """
    return sum(s) / len(s)


def different_elements(l1: list[int], l2: list[int]) -> int:
    """
    Retorna la quantitat d'elements de la combinacio de dues llistes (l1, l2),
    sense repeticions
    """
    return len(set(l1) | set(l2))


def has_duplicates(L: list[int]) -> bool:
    """
    Retorna si una llista (L) conte elements repetits, o no
    """
    return len(L) != len(set(L))


def extraneous(l1: list[str], l2: list[str]) -> str:
    """
    Donades una llista (l1) i una permutació d'aquesta amb un element afegit
    (l2), retorna l'element afegit
    """
    return (set(l2) - set(l1)).pop()


def extraneous_maybe(l1: list[str], l2: list[str]) -> Optional[str]:
    """
    Donades una llista (l1) i una permutació d'aquesta, que potser té un
    element afegit (l2), retorna l'element afegit, o None si no hi es
    """
    if set(l2) - set(l1):
        return list(set(l2) - set(l1))[0]


def different_words(s: str) -> int:
    """
    Donat un text (s), retorna la quantitat de paraules diferents al text,
    sense considerar capitalizació
    """
    return len(set(s.lower().split()))
