from yogi import read

formula = read(str)
index = 0

def solve_bool(exp: str, neg: bool) -> bool:
    if exp == "0" or exp == "1":
        return exp
    


print(solve_bool(formula,False))


