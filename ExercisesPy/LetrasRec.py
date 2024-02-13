from yogi import read

def print_patro_recursiu(a: str) -> str:
    letters = ["a","b","c","d","e","f","g","h","i","j"]
    #letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    b = 0
    for i in letters:
        if i == a:
            n = b
        b = b+1

    if n == 0:
        return "a"
    else:
        return (n*(letters[n]+print_patro_recursiu(letters[n-1]))) + letters[n]

if __name__ == "__main__":
    a = read(str)
    print(print_patro_recursiu(a))
