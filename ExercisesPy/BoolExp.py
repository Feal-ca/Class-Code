from yogi import read

def parentheses_interval(s: str)->int:
    open, closed = 0,0
    i = 0
    for char in s:
        if char == "(":
            open = open + 1
        if char == ")":
            closed = closed + 1
        if closed == open:
            break
        i = i +1
    return i


def bool_expression(exp: str,neg: bool) -> bool:
    c = exp[0]
    #print(exp)
    if c == "!":
        neg = not neg
        return (bool_expression(exp[1::],neg))
    if c == "(":
        a = parentheses_interval(exp)
        if neg:
            if bool_expression(exp[1:a], False):
                par = "0"
            else:
                par = "1"
        else:
            if bool_expression(exp[1:a],False):
                par = "1"
            else:
                par = "0"

        return bool_expression(par+exp[a+1::], False)

    if c == "0" or c=="1":
        if neg:
            if c == "0":
                c = "1"
            else:
                c = "0"
            neg = not neg

        try:
            operator = exp[1]
        except:
            return (c=="1")

        if exp[1]=="+":
            return bool(c=="1") or bool_expression(exp[2::],neg)
        if exp[1]=="*":
            return bool(c=="1") and bool_expression(exp[2::],neg)

if __name__ == "__main__":
    s = read(str)
    #print(parentheses_interval(s))
    if bool_expression(s,False):
        print("1")
    else:
        print("0")
