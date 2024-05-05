import fileinput
from typing import TypeAlias

Stack: TypeAlias = list[tuple[int, int]]

def quicksort(array: list[str]) -> None:
    """
    Sorts the given array in non-descending order
    """
    
    quicksort_it(array)


def quicksort_it(array: list[str]) -> None:
    """
    Sorts the given aray in non-descending order using
    an iterative quicksort approach
    """

    stack: Stack = [(0, len(array) -1)]

    while stack: 
        
        left, right = stack.pop()

        if left < right: # Recursive step
            mid: int = partition(array, left, right)

            stack.append((left, mid))
            stack.append((mid+1, right))
    
        
def partition(array: list[str], left: int, right: int) -> int:
    """
    Given a list (array) and two indeces (left, right), returns an index and
    partitions it in two halves, left one <= than the index and one >
    """

    pivot = array[left]
    i, j = left - 1, right + 1
    while True:
        while True:
            i += 1
            if array[i] >= pivot: break
        while True:
            j -= 1
            if array[j] <= pivot: break
        if i >= j:
            return j
        array[i], array[j] = array[j], array[i]


def main() -> None:
    for line in fileinput.input():
        array = line.strip().split()
        quicksort(array)
        print(*array)


if __name__ == "__main__":
    main()
