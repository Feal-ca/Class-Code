from __future__ import annotations
from dataclasses import dataclass
from typing import Iterator
from yogi import read


@dataclass
class Node:
    data: int
    left: BinTree
    right: BinTree


BinTree = Node | None


def read_tree() -> BinTree:
    x = read(int)
    if x == -1:
        return None
    else:
        return Node(x, read_tree(), read_tree())


def leaves(t: BinTree) -> Iterator[int]:
    if t is not None:
        if t.left is None and t.right is None:
            yield t.data

        yield from leaves(t.left)
        yield from leaves(t.right)

# def zipExtend(a: list[int], b: list[int]) -> Iterator[tuple[int,int]]:

def same_leaves(t1: BinTree, t2: BinTree) -> bool:
    return list(leaves(t1)) == list(leaves(t2))


def main():
    for _ in range(read(int)):
        t1, t2 = read_tree(), read_tree()
        print(*leaves(t1), ",", *leaves(t2), ",", same_leaves(t1, t2))


if __name__ == "__main__":
    main()
