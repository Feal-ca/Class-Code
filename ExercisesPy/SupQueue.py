from yogi import read, tokens
from dataclasses import dataclass
import time
import heapq


@dataclass(eq=False)
class Soldier:
    name: str
    enters: float
    rank: int

    def __gt__(self, other):
        if self.rank == other.rank:
            return self.enters > other.enters
        return self.rank < other.rank

    def __lt__(self, other):
        if self.rank == other.rank:
            return self.enters < other.enters
        return self.rank > other.rank

    def __ge__(self, other):
        if self.rank == other.rank:
            return self.enters >= other.enters
        return self.rank <= other.rank

    def __le__(self, other):
        if self.rank == other.rank:
            return self.enters <= other.enters
        return self.rank >= other.rank


def rank(s: str):
    return ["soldier", "sergeant", "captain", "colonel"].index(s)


def main():
    n = read(int)
    cues = [[] for _ in range(n)]

    for i in range(n):
        cua = input("").split()
        for nom in range(len(cua) // 2):
            r = rank(cua[2 * nom + 1])
            heapq.heappush(cues[i], Soldier(cua[2 * nom], time.time(), r))

    print("DEPARTS\n-------")
    for action in tokens(str):
        match action:
            case "LEAVES":
                n_cua = read(int) - 1
                if (0 <= n_cua <= n - 1) and cues[n_cua]:
                    departs = heapq.heappop(cues[n_cua])
                    print(departs.name)

            case "ENTERS":
                soldier = Soldier(read(str), time.time(), rank(read(str)))
                n_cua = read(int) - 1
                if 0 <= n_cua <= n - 1:
                    heapq.heappush(cues[n_cua], soldier)

    print("\nFINAL CONTENTS\n--------------")
    for i in range(len(cues)):
        print(f"queue {i+1}:", end="")
        while cues[i]:
            print(" " + heapq.heappop(cues[i]).name, end="")
        print()


if __name__ == "__main__":
    main()
