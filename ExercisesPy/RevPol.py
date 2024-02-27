def evaluate_exp(e):
    queue = []
    for s in e:
        if s == "+":
            queue.append(queue.pop() + queue.pop())
        elif s == "-":
            queue.append((-1) * queue.pop() + queue.pop())
        elif s == "*":
            queue.append(queue.pop() * queue.pop())
        else:
            queue.append(int(s))

    print(queue[0])


def main() -> None:
    while True:
        a = input().split(" ")
        evaluate_exp(a)


if __name__ == "__main__":
    main()
