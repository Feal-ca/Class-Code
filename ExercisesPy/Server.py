from yogi import read, tokens
from dataclasses import dataclass


@dataclass
class Server:
    id: str
    jobs: list[int]


def show_servers(servers):
    for s in servers:
        print(s.id, s.jobs)


def find(target, servers) -> Server:
    for s in servers:
        if s.id == target:
            return s


def add_task(s, value) -> None:
    added = False
    i = 0
    while not added and i < (len(s.jobs)):
        if s.jobs[i] > value:
            s.jobs.insert(i, value)
            added = True
        i += 1

    if not added:
        s.jobs.append(value)


def print_max_task(s) -> None:
    if s.jobs:
        print(s.jobs[-1])
    else:
        print("-")


def main() -> None:
    n = read(int)
    servers: list[Server] = [Server(read(str), []) for _ in range(n)]
    maxim = -1

    for action in tokens(str):
        match action:
            case "ADD":
                server_id = read(str)
                job_value = read(int)

                server = find(server_id, servers)

                if server:
                    add_task(server, job_value)
                    print_max_task(server)
                else:
                    print("identificador incorrecte")

            case "EXECUTE":
                server_id = read(str)
                q = read(int)

                server = find(server_id, servers)

                if server:
                    i = 0
                    while server.jobs and i < q:
                        maxim = max(server.jobs.pop(), maxim)
                        i += 1

                    print_max_task(server)

                else:
                    print("identificador incorrecte")

            case "TRANSFER":
                server_id1 = read(str)
                server_id2 = read(str)

                server1 = find(server_id1, servers)
                server2 = find(server_id2, servers)

                if server1 and server2:
                    if server1.jobs:
                        add_task(server2, server1.jobs.pop())

                    if server1.jobs:
                        print(server1.jobs[-1], end=" ")
                    else:
                        print("-", end=" ")
                    print_max_task(server2)

                else:
                    print("identificador incorrecte")

    print(f"\nMAX VALUE: {maxim}")
    print("\nPENDING:")
    for s in sorted(servers, key=lambda x: x.id):
        print(s.id, end=": ")
        print_max_task(s)


if __name__ == "__main__":
    main()
