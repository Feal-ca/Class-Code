from yogi import read, tokens
from typing import TypeAlias


Players: TypeAlias = dict[str, int]


def erase_player(ps: Players, p: str) -> None:
    if p in ps:
        print(f"{p} has won {ps[p]}")
        del ps[p]
    else:
        print(f"{p} is not in the casino")


def get_money(ps: Players, p: str, n: int) -> None:
    if p in ps:
        ps[p] += n
    else:
        print(f"{p} is not in the casino")


def new_player(ps: Players, p: str) -> None:
    if p not in ps:
        ps[p] = 0
    else:
        print(f"{p} is already in the casino")


def write_players(ps: Players) -> None:
    for p, money in sorted(ps.items()):
        print(f"{p} is winning {money}")


def main():
    players: Players = {}

    for name in tokens(str):
        instr = read(str)

        if instr == "enters":
            new_player(players, name)

        if instr == "leaves":
            erase_player(players, name)

        if instr == "wins":
            get_money(players, name, read(int))

    print("-" * 10)
    write_players(players)


if __name__ == "__main__":
    main()
