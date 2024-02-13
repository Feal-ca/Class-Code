from yogi import read, tokens
from dataclasses import dataclass
from functools import cmp_to_key


@dataclass
class Paraula:
    word: str
    freq: int


def compara(p1: Paraula, p2: Paraula) -> int:
    if p1.freq != p2.freq:
        return p2.freq - p1.freq

    if p1.word > p2.word:
        return 1
    elif p1.word < p2.word:
        return -1
    else:
        return 0


def main():
    for n in tokens(int):
        k = read(int)
        par = sorted([read(str) for _ in range(n)])
        words: list[Paraula] = []
        i = 0
        while i < n:
            c = 1
            j = i + 1
            while j < n and par[j] == par[i]:
                c += 1
                j += 1
            words.append(Paraula(par[i], c))
            i = j

        freq = sorted(words, key=cmp_to_key(compara))
        for i in range(k):
            print(freq[i].word)
        print("----------")


if __name__ == "__main__":
    main()
