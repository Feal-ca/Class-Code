from yogi import read
while True:
    n1 = read(int)
    n2 = read(int)
    result = 0.0
    while n1>n2:
        result = result + (1/n1)
        n1 = n1-1

    print("{:.10f}".format(result))