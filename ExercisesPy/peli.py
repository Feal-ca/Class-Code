from dataclasses import dataclass


@dataclass
class Movie:
    title: str
    year: int
    stars: int
    earnings: float


def compare_movies(m1: Movie, m2: Movie) -> int:
    result = 0
    if m1.stars != m2.stars:
        result = m2.stars-m1.stars
    elif m1.earnings != m2.earnings:
        result = m2.earnings - m1.earnings
    else:
        result = m2.year - m1.year

    if result > 0:
        return 1
    elif result < 0:
        return -1
    else:
        return 0
