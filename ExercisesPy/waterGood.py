from collections import deque
from typing import TypeAlias, Iterator
from yogi import read




def areEqual(d1,d2) -> bool:
    return all(e1 == e2 or e1 == -1 or e2 == -1 for e1, e2 in zip(d1, d2))

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

def bfs(caps, start, end):

    visited = set()
    visited.add(start)
    queue = deque()
    queue.append((start,0))

    while queue:
        state, d = queue.popleft()

        if areEqual(state, end):
            return 0

        for neigh in neighbors(caps, state):
            if neigh not in visited:
                visited.add(neigh)
                queue.append((neigh, d + 1))
    return -1


if __name__ == "__main__":
    N = read(int)
    caps = tuple(read(int) for _ in range(N))
    start = tuple(read(int) for _ in range(N))
    end = tuple(read(int) for _ in range(N))
    print(bfs(caps, start, end))
