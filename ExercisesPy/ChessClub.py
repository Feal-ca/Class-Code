from yogi import read, tokens


def main():
    n = read(int)
    white = {}
    black = {}
    for _ in range(n):
        w, b = read(str), read(str)
        if w not in white:
            white[w] = []
        white[w].append(b)

        if b not in black:
            black[b] = []
        black[b].append(w)

    for a in tokens(str):
        b = read(str)

        if a == "?":
            print(f"{b} has played black against:")
            for p in sorted(black[b]):
                print(p)

        else:
            print(f"{a} has played white against:")
            for p in sorted(white[a]):
                print(p)

        print()


if __name__ == "__main__":
    main()
