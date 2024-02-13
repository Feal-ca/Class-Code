from yogi import tokens

b = 2
def bigger_than_10(n:int) -> str:
    nums = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    return nums[n]

def recursive_basis(n: int,b: int):
    if n<b:
        return str(bigger_than_10(n))
    return recursive_basis(n//b,b)+str(bigger_than_10(n%b))


for n in tokens(int):
    print(f"{n} = {recursive_basis(n,2)}, {recursive_basis(n,8)}, {recursive_basis(n,16)}")

