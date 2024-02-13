from dataclasses import dataclass
from yogi import read, tokens
from functools import cmp_to_key


@dataclass
class Song:
    nom: str
    artist: str
    times: int
    length: int


@dataclass
class Artista:
    nom: str
    total: int


def comp1(s1: Song, s2: Song) -> int:
    if s1.artist > s2.artist:
        return 1
    elif s1.artist < s2.artist:
        return -1
    return 0


def comp2(a1: Artista, a2: Artista) -> int:
    if a2.total != a1.total:
        return a2.total-a1.total
    else:
        if a2.nom < a1.nom:
            return 1
        else:
            return -1


def comp3(s1: Song, s2: Song) -> int:
    if s2.times != s1.times:
        return s2.times-s1.times
    else:
        if s2.nom < s1.nom:
            return 1
        else:
            return -1


def sum_minutes(songs: list[Song]) -> int:
    """
    Calcula quants minuts s'han escoltat en total,
    donada una llista de cançons.
    """
    sum = 0
    for c in songs:
        sum += c.length*c.times

    return sum//60


def compute_top_artists(songs: list[Song]) -> list[str]:
    """
    Calcula els 5 artistes més escoltats dins la llista de cançons.
    Precondició: hi ha 5 o més artistes diferents.
    """

    artists: list[Artista] = []
    for c in sorted(songs, key=(cmp_to_key(comp1))):
        if artists != [] and c.artist == artists[-1].nom:
            artists[-1].total += c.length*c.times
        else:
            artists.append(Artista(c.artist, c.times*c.length))

    artists = sorted(artists, key=cmp_to_key(comp2))
    artistes_top = []

    for i in range(5):
        artistes_top.append(artists[i].nom)

    return artistes_top


def compute_top_songs(songs: list[Song]) -> list[str]:
    """
    Calcula les 5 cançons que més cops s'han escoltat de la llista de cançons.
    Precondició: hi ha 5 o més cançons diferents.
    """
    s = sorted(songs, key=cmp_to_key(comp3))
    songs_top = []

    for i in range(5):
        songs_top.append(s[i].nom)

    return songs_top


def main():
    n = read(int)
    songs = [Song(read(str), read(str), read(int), read(int))
             for c in range(n)]

    for request in tokens(str):
        if request == "minutes":
            print(f"Total de minuts escoltats: {sum_minutes(songs)}")
        elif request == "artists":
            print("Top 5 artists: " +
                  " ".join([str(x) for x in compute_top_artists(songs)]))
        else:

            print("Top 5 songs: " +
                  " ".join([str(x) for x in compute_top_songs(songs)]))


if __name__ == "__main__":
    main()
