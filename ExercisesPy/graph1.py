from yogi import tokens, read


def dfs(g, v, s, e):
    v.add(s)
    if s == e:
        return True
    for n in g[s]:
        if n not in v and dfs(g, v, n, e):
            return True
    return False


def main():
    n = read(int)
    graph = {read(str): [] for _ in range(n)}
    m = read(int)
    for _ in range(m):
        u = read(str)
        graph[u].append(read(str))

    s, e = read(str), read(str)
    if dfs(graph, set(), s, e):
        print("yes")
    else:
        print("no")


if __name__ == "__main__":
    main()
