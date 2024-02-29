from yogi import tokens

paraules: set[str] = set()
for paraula in tokens(str):
    paraula = paraula.lower()  # transforma paraula a minúscules
    paraules.add(paraula)

for paraula in sorted(paraules):
    print(paraula)
