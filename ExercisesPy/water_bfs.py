from yogi import read, tokens
from collections import deque

def neighbors(caps, dist):
    for i in range(len(dist)):
        if dist[i] != 0:
            for j in range(len(dist)):
                if dist[j] < caps[j] and i != j:
                    transfer = min(dist[i], caps[j]-dist[j])
                    res = list(dist)
                    res[i] -= transfer
                    res[j] += transfer
                    yield tuple(res)

def areEqual(d1,d2) -> bool:
    return all(e1 == e2 or e1 == -1 or e2 == -1 for e1, e2 in zip(d1, d2))

def bfs(caps, dist, obj):
    queue = deque([(dist, 0)])
    visited = set()

    while queue:
        current, d = queue.popleft()

        if areEqual(current, obj):
            return d

        for neigh in neighbors(caps, current):
            if neigh not in visited:
                visited.add(neigh)
                queue.append((neigh, d + 1))

    return -1


def main():
    n = read(int)
    caps = tuple(read(int) for _ in range(n))
    ini = tuple(read(int) for _ in range(n))
    fin = tuple(read(int) for _ in range(n))
    s = bfs(caps, ini, fin)

    print(s)


if __name__ == "__main__":
    main()

