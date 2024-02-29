from dataclasses import dataclass
from yogi import read, tokens


@dataclass
class points:
    wins: int
    loses: int
    draws: int


def main():
    players: dict[str, points] = {}
    n = read(int)

    for _ in range(n):
        s = read(str)
        if s not in players:
            players[s] = points(0, 0, 0)

    for white in tokens(str):
        black = read(str)

        result = read(str).split("-")

        if result[0] == "1":
            players[white].wins += 1
            players[black].loses += 1

        elif result[0] == "1/2":
            players[white].draws += 1
            players[black].draws += 1

        else:
            players[black].wins += 1
            players[white].loses += 1

    for player, results in sorted(players.items()):
        print(player, results.wins, results.draws, results.loses)


if __name__ == "__main__":
    main()
