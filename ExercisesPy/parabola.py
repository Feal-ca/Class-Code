from yogi import read, tokens

def draw_parabola(a: int, b: int, c: int, d: int) -> None:
    for i in range(d+1):
        n = (a*(i*i))+(b*i)+c
        print(n*"X")

    print("----------")
def main():
    for a in tokens(int):
        b = read(int)
        c = read(int)
        d = read(int)

        draw_parabola(a,b,c,d)


if __name__ == "__main__":
    main()
