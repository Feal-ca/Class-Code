from yogi import tokens

def es_primer(n):
    if n==0 or n==1:
        return False
    i = 2
    while i*i<=n:
        if n%i == 0:
            return False
        i = i+1
    return True

if __name__ == "__main__":
    for a in tokens(int):
        print(es_primer(a))
