from yogi import read, tokens


def select(k: int, A: list[int], B: list[int]) -> int:
    # l1, r1 = 0, len(A) - 1
    # l2, r2 = 0, len(B) - 1
    # return select_rec(k, A, B)

    l1, r1 = 0, len(A) - 1
    l2, r2 = 0, len(B) - 1

    while True:

        print(l1, r1)
        print(l2, r2)
        if l1 > r1:
            return B[l2 + k - 1]
        if l2 > r2:
            return A[l1 + k - 1]

        mid1 = (l1 + r1) // 2
        mid2 = (l2 + r2) // 2

        if (mid1-l1+1  + mid2-l2+1) <= k:
            if A[mid1] > B[mid2]:
                k -= mid2 - l2 + 1
                l2 = mid2 + 1
            else:
                k -= mid1 - l1 + 1
                l1 = mid1 + 1
        else:
            if A[mid1] > B[mid2]:
                r1 = mid1 - 1
            else:
                r2 = mid2 - 1

for n in tokens(int):
    A: list[int] = [read(int) for _ in range(n)]
    m: int = read(int)
    B: list[int] = [read(int) for _ in range(m)]
    t: int = read(int)
    for _ in range(t):
            k: int = read(int)
            print(select(k, A, B))

