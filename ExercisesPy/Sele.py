from yogi import read
from dataclasses import dataclass
from typing import Optional


@dataclass
class Estudiant:
    nom: str
    dni: int
    nota: float
    preferencies: list[str]
    assignacio: Optional[str]


def llegir_estudiant() -> Estudiant:
    return Estudiant(read(str), read(int), read(float), read(str).split(","), None)


def llegir_estudiants() -> list[Estudiant]:
    return [llegir_estudiant() for _ in range(read(int))]


@dataclass
class Titulacio:
    nom: str
    places: int
    nota_de_tall: float


def llegir_titulacio() -> Titulacio:
    return Titulacio(read(str), read(int), 0.0)


def llegir_titulacions() -> list[Titulacio]:
    return [llegir_titulacio() for _ in range(read(int))]


def assignacio(e: Estudiant, ts: list[Titulacio]) -> Optional[str]:
    for eleccio in e.preferencies:
        for t in ts:
            if t.nom == eleccio and t.places > 0:
                t.places -= 1
                t.nota_de_tall = e.nota
                return eleccio


def assignar(estudiants: list[Estudiant], titulacions: list[Titulacio]) -> None:
    estudiants.sort(key=lambda p: (-p.nota, p.dni))
    for e in estudiants:
        e.assignacio = assignacio(e, titulacions)


def escriure_assignacio(estudiants: list[Estudiant]) -> None:
    print("---")
    for e in sorted(estudiants, key=lambda x: x.dni):
        print(e.dni, e.nom, e.assignacio)


def escriure_notes_de_tall(titulacions: list[Titulacio]) -> None:
    print("---")
    for t in sorted(titulacions, key=lambda x: (-x.nota_de_tall, x.nom)):
        print(t.nom, t.nota_de_tall, t.places)


def main() -> None:
    estudiants = llegir_estudiants()
    titulacions = llegir_titulacions()
    assignar(estudiants, titulacions)
    escriure_assignacio(estudiants)
    escriure_notes_de_tall(titulacions)


if __name__ == "__main__":
    main()
