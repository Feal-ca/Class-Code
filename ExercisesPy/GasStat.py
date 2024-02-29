from yogi import read, tokens


def minimum_required_range(s: int, cs: list[int]) -> int:
    ...


def main():
    n = read(int)
    s = read(int)

    cs = [read(int) for _ in range(n)]

    print(minimum_required_range(s, cs))


if __name__ == "__main__":
    main()
