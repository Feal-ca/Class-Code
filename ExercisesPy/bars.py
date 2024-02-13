from yogi import read

def bars_I(n: int):
    if n>0:
        bars_I(n-1)
        print(n*'*')
        bars_I(n-1)

def bars_II(n: int):
    if n>0:
        print(n*'*')
        bars_II(n-1)
        bars_II(n-1)

def bars_III(n: int):
    if n>0:
        bars_III(n-1)
        bars_III(n-1)
        print(n*'*')
if __name__ == "__main__":
    n = read(int)
    bars_III(n)
