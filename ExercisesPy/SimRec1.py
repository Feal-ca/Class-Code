from yogi import tokens


def work(n: int) -> None:
    stack = []
    while n > 0 or stack:
        if n > 0:
            stack.append(n)
            n -= 1
        else:
            n = stack.pop() - 1
            print("", n + 1, end="")


def main() -> None:
    for n in tokens(int):
        work(n)
        print()


if __name__ == "__main__":
    main()
