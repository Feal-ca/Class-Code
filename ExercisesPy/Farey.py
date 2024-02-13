from yogi import tokens


def show_farey(n: int) -> None:
    a, b, c, d = 0, 1, 1, n
    e, f, x = 0, 0, 0
    print(f"0/1 1/{n}", end="")
    if c == 1 and d == 1:
        pass
    else:
        while e != 1 or f != 1:
            x = int((n + b) / d)
            e = (x * c) - a
            f = (x * d) - b
            print(f" {e}/{f}", end="")
            a, b = c, d
            c, d = e, f
    print()


if __name__ == "__main__":
    for n in tokens(int):
        show_farey(n)
