from yogi import read

def print_bars(n: int, b: int)->None:
    print(10*"-")

    while n>0:
        print((n%b)*"X")
        n = n//b

    print(10*"-")


if __name__ == "__main__":
    num = read(int)
    base = read(int)
    print_bars(num, base)
