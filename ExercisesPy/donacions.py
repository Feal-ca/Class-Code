from yogi import read, tokens

def main() -> None:
    num_donors = 0
    max_donor = None
    donors_amount: dict[str, int] = dict()
    for instr in tokens(str):
        # print(instr)
        match instr:
            case "N":
                print(f"number: {num_donors}")

            case "D":
                n, m = read(str), read(int)
                if n in donors_amount:
                    donors_amount[n] = donors_amount[n] + m
                else:
                    donors_amount[n] = m
                    num_donors += 1
                    if max_donor is None or n>max_donor:
                        max_donor = n

            case "Q":
                n = read(str)
                donation = donors_amount.get(n, -1)
                print(donation)

            case "P":
                print(*sorted([nif for nif in filter(lambda x: int(x[-2])%2==0, donors_amount.keys())]))

            case "L":
                if max_donor is not None:
                    print(max_donor, donors_amount[max_donor])
                else:
                    print(None)

if __name__ == "__main__":
    main()
