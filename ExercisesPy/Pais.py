from typing import TypeAlias
from dataclasses import dataclass


@dataclass
class Provincia:
    nom: str
    capital: str
    habitants: int
    area: int
    pib: float


@dataclass
class Pais:
    nom: str
    capital: str
    provincies: list[Provincia]


Paisos: TypeAlias = list[Pais]


def pib(paisos: Paisos, inicial: str, densitat: float) -> float:
    pibs = 0.0
    for p in paisos:
        if p.nom[0] == inicial:
            for pr in p.provincies:
                if pr.habitants / pr.area > densitat:
                    pibs += pr.pib
    return pibs


def pib2(paisos: Paisos, inicial: str, densitat: float) -> float:
    pibs = sum(
        [
            pr.pib
            for p in paisos
            if p.nom[0] == inicial
            for pr in p.provincies
            if (pr.habitants / pr.area) > densitat
        ]
    )
    return float(pibs)


def habitants(paisos: Paisos, x: float) -> int:
    hab_total = 0
    for p in paisos:
        prov_valides = [prov for prov in p.provincies if prov.pib <= x]
        if len(prov_valides) >= 2:
            for pr in p.provincies:
                hab_total += pr.habitants

    return hab_total


p1 = Pais(
    "ala",
    "CapitalA",
    [
        Provincia("Prov1", "Cap1", 1, 9, 5),
        Provincia("Prov2", "Cap2", 10000, 9, 37),
        Provincia("Prov3", "Cap3", 1000, 9, 125),
    ],
)
p2 = Pais(
    "bla",
    "CapitalB",
    [
        Provincia("Prov4", "Cap4", 1, 9, 5),
        Provincia("Prov5", "Cap5", 10000, 9, 37),
        Provincia("Prov6", "Cap6", 1000, 9, 125),
    ],
)
p3 = Pais(
    "ab",
    "CapitalC",
    [
        Provincia("Prov7", "Cap7", 1000, 9, 99),
        Provincia("Prov8", "Cap8", 10000, 9, 37),
        Provincia("Prov9", "Cap9", 1000, 9, 125),
    ],
)
print(habitants([p1, p2, p3], 80))
