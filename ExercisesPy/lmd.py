import math

n = 1.0
while n<100000000:
    if (n/2)**(1.0/2) == int((n/2)**(1.0/2)):
        if (n/3)**(1.0/3) == int((n/3)**(1.0/3)):
            if (n/5)**(1.0/5) == int((n/5)**(1.0/5)):
                print(n)
                print("Funciona ^^^")
    n = n+1

