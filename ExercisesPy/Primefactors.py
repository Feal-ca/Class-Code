def escriure_factors_primers(n):
    factors=[]
    fct = ""
    if n!=1:
        b=2
        while n>=b:
            if n%b==0:
                if b not in factors:
                    factors.append(b)
                n = n//b
            else:
                b=b+1
        for i in factors[:-1]:
            fct = fct+str(i)+","
        fct = fct+ str(factors[len(factors)-1])
    print(fct)
