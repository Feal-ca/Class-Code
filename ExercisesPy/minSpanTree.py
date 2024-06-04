from yogi import read, tokens
from collections import deque
import heapq

def minSpanTree(G, size, m) -> int:
    visited = [False for _ in range(size)]
    prev = [-1 for _ in range(size)]

    visited[0] = True
    n = 1

    Q: list[tuple[int,int,int]] = []
    min_cost = 0

    for cost, v in G[0]:
        heapq.heappush(Q, (cost, 0, v))

    while n < size:
        (cost, u,v) = heapq.heappop(Q)
        if not visited[v]:
            visited[v] = True
            prev[v] = u
            n = n+1
            min_cost += cost
            for cost, x in G[v]:
                if not visited[x]:
                    heapq.heappush(Q, (cost, v, x))

    return min_cost

def main():
    for n in tokens(int):
        m = read(int)
        G = {i:[] for i in range(n)}
        for _ in range(m):
            u,v,cost = read(int) - 1, read(int) - 1, read(int)
            G[u].append((cost, v))
            G[v].append((cost, u))

        w = minSpanTree(G, n, m)
        print(w)

if __name__ == "__main__":
    main()
