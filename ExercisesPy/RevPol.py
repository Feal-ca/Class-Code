from dataclasses import dataclass


def evaluate_exp(e: list[str]) -> None:
    ue = []
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
        a = input()
        a = a.split(" ")
        evaluate_exp(a)


if __name__ == "__main__":
    main()
