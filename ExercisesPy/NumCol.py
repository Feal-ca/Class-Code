import heapq
from yogi import tokens, read


def main() -> None:
    cuap = []
    sum = 0
    size = 0
    is_first = True

    for w in tokens(str):
        if w == "S":
            n = read(int)
            heapq.heappush(cuap, -n)

        elif w == "A":
            if cuap:
                print(-cuap[0])
            else:
                print("error!")

        elif w == "R":
            if cuap:
                heapq.heappop(cuap)
            else:
                print("error!")
        elif w == "I":
            if cuap:
                x = read(int)
                n = heapq.heappop(cuap)
                heapq.heappush(cuap, n - x)
            else:
                print("error!")

        elif w == "D":
            if cuap:
                x = read(int)
                n = heapq.heappop(cuap)
                heapq.heappush(cuap, n + x)
            else:
                print("error!")


if __name__ == "__main__":
    main()
