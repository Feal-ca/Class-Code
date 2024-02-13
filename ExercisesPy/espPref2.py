from yogi import read

def is_num(n: str)->bool:
    if n !=" " or n!="*" or n!="-" or n!="+":
        return True
    return False


def solve_exp2()-> int:
    a = read(str)
    if a == "+":
        return solve_exp2() + solve_exp2()

    elif a == "m":
        return max(solve_exp2(), solve_exp2(), solve_exp2())

    elif a == "-":
        return (-1) * solve_exp2()

    elif a == "*":
        return solve_exp2() * solve_exp2()
    else:
        return int(a)

def solve_exp()-> int:
    a = read(str)
    if a == "+":
        return solve_exp() + solve_exp()

    elif a == "-":
        return solve_exp() - solve_exp()

    elif a == "*":
        return solve_exp() * solve_exp()
    else:
        return int(a)
if __name__ == "__main__":
    print(solve_exp2())
