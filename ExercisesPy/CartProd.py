def cartesian_product(a: set[int], b: set[int]) -> set[tuple[int, int]]:
    return sorted(list({(x, y) for x in a for y in b}))


def main():
    print(cartesian_product(set([1, 3, 5, 6]), set([1, 2, 3])))


if __name__ == "__main__":
    main()
