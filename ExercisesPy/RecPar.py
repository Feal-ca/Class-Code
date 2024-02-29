from yogi import tokens

# crear el diccionari comptador d'ocurrències de paraules buit
ocurrencies: dict[str, int] = {}

# llegir cada paraula i afegir-la al diccionari
for paraula in tokens(str):
    paraula = paraula.lower()
    if paraula not in ocurrencies:
        ocurrencies[paraula] = 1
    else:
        ocurrencies[paraula] += 1

# recórrer els elements del diccionari per escriure'ls
for paraula, comptador in sorted(ocurrencies.items(), key=lambda x: (x[1], x[0])):
    print(comptador, paraula)
