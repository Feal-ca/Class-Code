import heapq
from yogi import tokens, read


def main() -> None:
    cuap = []
    sum = 0
    size = 0
    is_first = True

    for w in tokens(str):
        if w == "number":
            n = read(int)
            heapq.heappush(cuap, n)
            if is_first:
                max_val = n
                is_first = False
            else:
                max_val = max(max_val, n)

            sum += n
            size += 1
        elif size != 0:
            sum -= heapq.heappop(cuap)
            size -= 1

        if size != 0:
            print(f"minimum: {cuap[0]}, maximum: {max_val}, average: {sum/size:.4f}")
        else:
            is_first = True
            print("no elements")


if __name__ == "__main__":
    main()
