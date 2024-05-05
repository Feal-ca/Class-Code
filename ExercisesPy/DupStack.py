import yogi
from typing import TypeAlias

StackInt: TypeAlias = list[int]


class NoDupsStack:
    """
    A stack of integers without any duplicate elements 
    """

    _stack: StackInt
    _elements: set[int]

    def __init__(self):
        """
        Initializes the NoDupsStack class
        """

        self._stack = []
        self._elements = set()

    def push(self, element: int) -> None:
        """
        Pushes an element to the stack if it's not already present
        """

        self._elements.add(element)
        if len(self._elements) != len(self._stack): 
            # The set has one more element now, so it must be a distinct element
            self._stack.append(element)
            
    def pop(self) -> None:
        """
        Removes an element from the stack.
        The stack cannot be empty
        """

        assert not self.empty()

        e = self._stack.pop()
        self._elements.remove(e)

    def top(self) -> int:
        """
        Returns the first element in the stack.
        The stack cannot be empty
        """

        assert not self.empty()

        return self._stack[-1]

    def empty(self) -> bool:
        """
        Checks if the stack is empty, returns True when it is
        """

        return not self._stack


def main() -> None:
    s = NoDupsStack()
    for command in yogi.tokens(str):
        if command == "push":
            s.push(yogi.read(int))
        elif command == "pop":
            s.pop()
        elif command == "top":
            print(s.top())
        elif command == "empty":
            print(s.empty())

if __name__ == "__main__":
    main()