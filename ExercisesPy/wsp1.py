from yogi import read, tokens
from collections import deque
import heapq

INF = 10**9

def short_path(G,s,e):
    ds = [INF for _ in range(len(G))]
    ds[s] = 0
    pq = [(0,s)]
    while pq:
        d,v = heapq.heappop(pq)
        if v == e: return d

        if d <= ds[v]:
            for w,neighbor in G[v]:
                newDist = d + w

                if newDist < ds[neighbor]:
                    ds[neighbor] = newDist
                    heapq.heappush(pq,(newDist, neighbor))

def main():
    for n in tokens(int):
        m = read(int)
        G = [[] for _ in range(n)]
        for _ in range(m):
            u,v,cost = read(int), read(int), read(int)
            G[u].append((cost,v))
        s,e = read(int),read(int)
        d = short_path(G,s,e)
        print(f"{d}" if d is not None else f"no path from {s} to {e}")

if __name__ == "__main__":
    main()
