from yogi import read, tokens
# from typing import Callable


def bin_search(arr: list[int], ref: int):
    left = 0
    right = sum(arr)
    while left <= right:
        mid = left + (right - left) // 2
        # print(mid)
        # print(gets_there(mid, arr, ref))

        if gets_there(mid, arr, ref):
            final = mid
            right = mid - 1

        else:
            left = mid + 1

    return final


def gets_there(rang: int, cs: list[int], refills: int) -> bool:
    r = rang
    i = 0
    while refills >= 0 and i < len(cs):
        if r >= cs[i]:
            r -= cs[i]
            i += 1

        else:
            refills -= 1
            r = rang

        #  print(r, i, cs[i], refills)
    return refills >= 0


def minimum_required_range(s: int, cs: list[int]) -> int:
    return bin_search(cs, s)


def main():
    for n in tokens(int):
        s = read(int)

        # print(gets_there(374, [100, 300, 500, 200, 400], 4))
        cs = [read(int) for _ in range(n)]
        print(minimum_required_range(s, cs))


if __name__ == "__main__":
    main()
