from yogi import read, tokens


def main() -> None:
    n = read(int)
    L = [x for x in tokens(int)]
    print(L)


if __name__ == "__main__":
    main()
