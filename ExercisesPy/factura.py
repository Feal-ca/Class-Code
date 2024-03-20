from yogi import read, tokens


def enesim_euro(e: int) -> str:
    """
    Llegeix una entrada de n arbitrari items y el seu preu, 
    y retorna l'item en que es va gastar l'euro numero (e)
    """
    total_price = 0
    
    item = "No gastado"
    for element in tokens(str):
        if element == "---":
            break
        price = read(int)
        
        total_price = total_price + price
        
        if total_price >= e and item == "No gastado": #Si l'item supera l'euro (e) i es el primer en fer-ho
            item = element
            
    return item
        
            
if __name__ == "__main__":
    n = read(int)
    e = read(int)
    
    for i in range(n):
        a = read(str)    
        item = enesim_euro(e)
        
        if item == "No gastado": # en lugar de None
            print(f"En la factura {a} no s'ha gastat l'euro {e}.")
        else:
            print(f"En la factura {a} l'euro {e} s'ha gastat en {item}.")
            
"""
4 130

mobils
samsung 600
iphone 1000
---
dinar
joan 30
maria 20
claudia 35
pere 40
josep 25
---
cafeteria
cafe 2
croissant 3
---
ordinadors
lenovo 600
hp 800
asus 500
---

"""
