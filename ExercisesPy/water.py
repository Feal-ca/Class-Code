from yogi import read, tokens
from collections import deque
import heapq

def heuristic(state, goal):
    r = 0
    for i, e in enumerate(state):
        if goal[i] != -1:
            r += abs(goal[i]-e)
    return r

def neighbors(caps, dist):
    return set(
        tuple(dist[t] - (t == i)*min(dist[i], caps[j]-dist[j]) + (j==t)*min(dist[i], caps[j]-dist[j]) for t in range(len(dist)))
        for i in range(len(dist))
        for j in range(len(dist))
    )

def areEqual(d1,d2) -> bool:
    return all(e1 == -1 or e2 == -1 or e1 == e2 for e1, e2 in zip(d1, d2))

def a_star_search(caps, dist, obj):
    frontier = []
    heapq.heappush(frontier, (0, dist))
    came_from = {dist: None}
    cost_so_far = {dist: 0}

    while frontier:
        d, current = heapq.heappop(frontier)
        if areEqual(current,obj):
            return d

        for neighbor in neighbors(caps, current):
            new_cost = cost_so_far[current] + 1
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, obj)
                heapq.heappush(frontier, (priority, neighbor))
                came_from[neighbor] = current

    return -1

def main():
    n = read(int)
    caps = tuple(read(int) for _ in range(n))
    ini = tuple(read(int) for _ in range(n))
    fin = tuple(read(int) for _ in range(n))
    s = a_star_search(caps, ini, fin)

    print(s)


if __name__ == "__main__":
    main()
