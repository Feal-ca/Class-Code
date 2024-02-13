from yogi import read


def has_null_marc(mat: list[list[int]], n: int, m: int) -> bool:
    for i in range(1, n+1):
        for j in range(1, m+1):
            mat[i][j] = read(int)
            mat[i][j] += mat[i][j-1] + mat[i-1][j] - mat[i-1][j-1]

            if mat[i][j] == 0:
                return True
    return False


def has_null_marc2(mat: list[list[int]], n: int, m: int) -> bool:
    for i in range(n):
        for j in range(m):
            if j != 0:
                mat[i][j] += mat[i][j-1]

            if i != 0:
                mat[i][j] += mat[i-1][j]

            if i != 0 and j != 0:
                mat[i][j] -= mat[i-1][j-1]
            if mat[i][j] == 0:
                return True
    return False


def main() -> None:
    n, m = read(int), read(int)
    # matrix = [[read(int) for _ in range(m)] for _ in range(n)]
    matrix = [[0 for _ in range(m+1)] for _ in range(n+1)]

    print(has_null_marc(matrix, n, m))


if __name__ == "__main__":
    main()
