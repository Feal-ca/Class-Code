from yogi import read, tokens
from collections import deque
import heapq

INF = 10**9

def path_to_end(d_p, e):
    r = [e]
    v = e
    while d_p[v][1] != None:
        p = d_p[v][1]
        r.append(p)
        v = p
    r.reverse()
    return r

def short_path(G,s,e):
    ds_pre = [[INF,None] for _ in range(len(G))]
    ds_pre[s][0] = 0

    pq = [(0,s)]

    while pq:
        d,v = heapq.heappop(pq)
        if v == e: return path_to_end(ds_pre, e)

        if d <= ds_pre[v][0]:
            for w,neighbor in G[v]:
                newDist = d + w

                if newDist < ds_pre[neighbor][0]:
                    ds_pre[neighbor][0] = newDist
                    ds_pre[neighbor][1] = v
                    heapq.heappush(pq,(newDist, neighbor))
    return []

def main():
    for n in tokens(int):
        m = read(int)
        G = [[] for _ in range(n)]
        for _ in range(m):
            u,v,cost = read(int), read(int), read(int)
            G[u].append((cost,v))
        s,e = read(int),read(int)
        d = short_path(G,s,e)
        if len(d) > 0:
            print(*d)
        else: print(f"no path from {s} to {e}")

if __name__ == "__main__":
    main()
