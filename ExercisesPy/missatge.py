def missatge(qui,verb,cops,fem):
    if fem: pr="Na"
    else: pr="En"
    if cops>1: s="s"
    else: s=""
    if cops==0:
        print(f"{pr} {qui} no ha {verb}.")
    else:
        print(f"{pr} {qui} ha {verb} {cops} cop{s}.")
