from yogi import read


def solve_hanoi(n:int,start: str, aux: str, end:str):
    if n>0:
        solve_hanoi(n-1,start,end,aux)
        print(f"{start} => {end}")
        solve_hanoi(n-1, aux, start, end)

if __name__ == "__main__":            
    n = read(int)
    solve_hanoi(n, 'A','B','C')
