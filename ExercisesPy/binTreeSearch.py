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

def isInBinTree(x: int, tree: BinTree) -> bool:
    """
    Returns True if (x) is in the Tree (tree), False otherwise
    """
    if tree is None:
        return False

    if x < tree[0]:
        return isInBinTree(x, tree[1])
    if x > tree[0]:
        return isInBinTree(x, tree[2])

    return True  # x == tree[0]

def main() -> None:
    read(int)  # Legacy code :(
    tree = getBinTree()

    for n in tokens(int):
        print(f"{n} 1" if isInBinTree(n, tree) else f"{n} 0")

if __name__ == "__main__":
    main()
