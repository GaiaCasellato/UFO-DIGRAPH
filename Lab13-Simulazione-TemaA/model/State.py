from dataclasses import dataclass


@dataclass
class State:
    Population: int
    Neighbors: str
    Name: str
    Lng: float
    Lat: float
    id: str
    Capital: str
    Area: float

    def __str__(self):
        return self.id

    def __hash__(self):
        return hash(self.id)