from yogi import read, tokens
from dataclasses import dataclass

@dataclass
class Card:
    """
    Information associated to a credit card
    """
    last_date: int
    money_spent: float
    items_bought: int


def is_valid_student(s: tuple[str,Card]) -> bool:
    """
    Returns True if the student (s) is a valid candidate
    """
    
    return s[1].last_date >= 20240301 and s[1].money_spent >= 200.0 and s[1].items_bought >= 3


def show_candidates(students: dict[str, Card]) -> None:
    """
    Prints to the screen the card ID of the valid candidates in (students) 
    """

    valid_students = sorted(filter(is_valid_student, students.items()), key = lambda x: x[0])

    for card, _ in valid_students:
        print(card)


def get_students() -> dict[str, Card]:
    """
    Reads input and returns a dictionary with the card ID as key,
    and  a (Card) with relevant info for candidacy as value 
    """

    students: dict[str, Card] = dict()

    for date in tokens(int):
        cardID, price = read(str), read(float)

        s = students.get(cardID, None) 

        if not s: # Initialize it
            students[cardID] = Card(date, price, 1)

        else: # Update the values
            s.last_date = date
            s.money_spent += price
            s.items_bought += 1

    return students


def main() -> None:

    students = get_students()
    show_candidates(students)


if __name__ == "__main__":
    main()