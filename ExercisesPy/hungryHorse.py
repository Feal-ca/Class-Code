from yogi import read,tokens
from collections import deque

def get_neighbors(c: tuple[int,int]) -> list[tuple[int,int]]:
    jumps = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]

    return [(c[0]+a, c[1]+b) for a,b in jumps]

def in_board(c, board)->bool:
    height_check = 0<= c[0] < len(board)
    width_check = 0<= c[1] < len(board[0])

    return height_check and width_check

def get_min_jumps(s: tuple[int,int], board) -> int:
    visited = set()
    queue = deque([(s,0)])
    visited.add(s)

    while queue:
        pos, d = queue.popleft()

        if board[pos[0]][pos[1]] == 'p':
            return d

        for n in get_neighbors(pos):
            if in_board(n, board) and board[n[0]][n[1]] != 'X' and n not in visited:
                visited.add(n)
                queue.append((n, d+1))
    return -1

def main() -> None:
    for rows in tokens(int):
        cols = read(int)
        board = [read(str) for _ in range(rows)]
        start = (read(int)-1, read(int)-1)
        min_jumps = get_min_jumps(start, board)
        print(f"{min_jumps}" if min_jumps != -1 else "no")
if __name__ == "__main__":
    main()
