from yogi import read

def print_octagon(n: int)-> None:
    for i in range(n):
        print((n-1-i)*" ",end="")
        print((n+(2*i))*"X")
    
    for i in range(n-2):
        print((n+(2*(n-1)))*"X")

    for i in range(n):
        print((i)*" ",end="")
        print((n+(2*(n-1-i)))*"X")

if __name__ == "__main__":
    while True:
        a = read(int)
        print_octagon(a)
        print()
