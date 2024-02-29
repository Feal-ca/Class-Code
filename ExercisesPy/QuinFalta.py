from yogi import tokens, read


def main():
    for n in tokens(int):
        k = read(int)
        bag = {read(int) for _ in range(k)}
        sum = (n * (n + 1)) // 2
        for item in bag:
            sum -= item

        print(sum)


if __name__ == "__main__":
    main()
