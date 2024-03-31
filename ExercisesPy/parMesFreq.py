from yogi import read, tokens
from dataclasses import dataclass
from functools import cmp_to_key


@dataclass
class Paraula:
    word: str
    freq: int


def main():
    for n in tokens(int):
        k = read(int)
        words = {}
        for _ in range(n):
            w = read(str)
            words[w] = words.get(w, 0) + 1

        freq = sorted(words.items(), key=lambda x: (-x[1], x[0]))

        for i in range(k):
            print(freq[i][0])
        print("----------")


if __name__ == "__main__":
    main()
