import heapq
from yogi import read, tokens


def main():
    for n in tokens(int):
        m = read(int)
        succ = {x: [] for x in range(n)}
        pre = {x: 0 for x in range(n)}

        for _ in range(m):
            u, v = read(int), read(int)
            succ[u].append(v)
            pre[v] += 1

        heap = [x for x in range(n) if pre[x] == 0]
        heapq.heapify(heap)

        while heap:
            node = heapq.heappop(heap)
            print(node, end="")

            for v in succ[node]:
                pre[v] -= 1
                if pre[v] == 0:
                    heapq.heappush(heap, v)

            if len(heap) != 0:
                print(" ", end="")

        print()


if __name__ == "__main__":
    main()

