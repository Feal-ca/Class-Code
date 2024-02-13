from yogi import scan

def pic():
    prev_h = scan(int)
    h = scan(int)
    next_h = scan(int)

    while next_h != 0:
        if h>3143 and h>prev_h and h>next_h:
            return "YES"
        prev_h=h
        h=next_h
        next_h = scan(int)
    return "NO"

if __name__ == "__main__":
    result = pic()
    print(result)
