from collections import deque
def parse(tokens):
    token=tokens.pop(0)
    print(tokens)
    if token=='+':
            return parse(tokens)+parse(tokens)
    elif token=='-':
            return parse(tokens)-parse(tokens)
    elif token=='*':
            return parse(tokens)*parse(tokens)
    elif token=='/':
            return parse(tokens)/parse(tokens)
    else:
            # must be just a number
            return int(token)


if __name__=='__main__':
        expression="* 3 + 2 3"
        print(parse((expression.split())))

