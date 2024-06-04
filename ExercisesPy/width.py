from yogi import read, tokens
from typing import TypeAlias, Optional

BinTree: TypeAlias = Optional['Node']
Node: TypeAlias = tuple[int, BinTree, BinTree]

def getBinTree() -> BinTree:
    """
    Reads the description of a tree and returns the built tree
    """
    x = read(int)
    if x == -1:
        return None
    return (x, getBinTree(), getBinTree())

def getKids(t: BinTree) -> list[BinTree]:
    return [t[i] for i in range(1,3) if t[i] is not None]

def main():
    n = read(int)

    for _ in range(n):
        tree = getBinTree()



if __name__ == "__main__":

    main()
