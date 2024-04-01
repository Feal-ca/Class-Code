from yogi import read, tokens
from typing import Iterator


def collatz(n: int) -> Iterator[int]:
    while n != 1:
        yield n
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    yield n


def collatz_length(n: int) -> int:
    i = 0
    for _ in collatz(n):
        i += 1
    return i


def collatz_highest(n: int) -> int:
    return max(collatz(n))


def collatz_highest_position(n: int) -> tuple[int, int]:
    index, maxim = 0, n
    i = 0
    for num in collatz(n):
        if num > maxim:
            maxim = num
            index = i
        i += 1

    return (index, maxim)


def collatz_11(n: int) -> bool:
    if n % 2 == 0:
        n2 = n / 2
    else:
        n2 = 3 * n + 1
    return any(x % 11 == 0 for x in collatz(n2))


def collatz_first_common(n1: int, n2: int) -> int:
    for x in collatz(n1):
        for y in collatz(n2):
            if x == y:
                return x


def collatz_common_elements(n1: int, n2: int) -> int:
    return sum(1 for x in collatz(n1) for y in collatz(n2) if x == y)


def collatz_union(n1: int, n2: int) -> list[int]:
    return sorted(list(set([x for x in collatz(n1)] + [y for y in collatz(n2)])))


def collatz_top_numbers() -> Iterator[int]:
    maxim = 0
    i = 0
    while True:
        i += 1
        n = collatz_highest(i)
        if n > maxim:
            maxim = n
            yield i


def collatz_first_missing(n: int) -> int:
    i = 0
    while True:
        i += 1
        if i not in collatz(n):
            return i


def main() -> None:
    """Main program"""

    for command in tokens(str):
        if command == "collatz":
            print(*list(collatz(read(int))))
        elif command == "collatz_length":
            print(collatz_length(read(int)))
        elif command == "collatz_highest":
            print(collatz_highest(read(int)))
        elif command == "collatz_highest_position":
            print(collatz_highest_position(read(int)))
        elif command == "collatz_11":
            print(collatz_11(read(int)))
        elif command == "collatz_first_common":
            print(collatz_first_common(read(int), read(int)))
        elif command == "collatz_common_elements":
            print(collatz_common_elements(read(int), read(int)))
        elif command == "collatz_union":
            print(*collatz_union(read(int), read(int)))
        elif command == "collatz_top_numbers":
            print(*[v for v, _ in zip(collatz_top_numbers(), range(read(int)))])
        elif command == "collatz_first_missing":
            print(collatz_first_missing(read(int)))
        else:
            assert False

main()
main()
