from yogi import read

def es_xupiguai(n: int, b: int)->bool:
    if (n%b) > (b//2) or (n%(b*b))<= (b//2):
        return False
    return es_xupiguai(n//b, b)

if __name__ == "__main__":
    while True:
        n = read(int)
        b = read(int)
        print(es_xupiguai(n,b)
