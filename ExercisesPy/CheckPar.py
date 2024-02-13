from yogi import tokens


def eval_exp(exp: str) -> bool:
    stack = []
    for c in exp:
        if c == "[" or c == "(":
            stack.append(c)
        else:
            if (len(stack) > 0) and (
                (c == ")" and stack[-1] == "(") or (c == "]" and stack[-1] == "[")
            ):
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False


def main() -> None:
    for exp in tokens(str):
        if eval_exp(exp):
            print(exp + " is correct")
        else:
            print(exp + " is incorrect")


if __name__ == "__main__":
    main()
