import math
from abc import ABC, abstractmethod
from typing import Mapping


class Vector:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"Vec({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"<Vec({self.x}, {self.y})>"

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other: "Vector") -> bool:
        if  not isinstance(other, Vector):
            raise NotImplementedError
    
        return self.x == other.x and self.y == other.y


class AbstractMovable(ABC):
    @property
    @abstractmethod
    def position(self) -> Vector:
        ...

    @position.setter
    @abstractmethod
    def position(self, vec: Vector) -> None:
        ...

    @property
    @abstractmethod
    def velocity(self) -> Vector:
        ...


class AbstractRotable(ABC):
    @property
    @abstractmethod
    def direction(self) -> int:
        ...

    @direction.setter
    @abstractmethod
    def direction(self, val: int) -> None:
        ...

    @property
    @abstractmethod
    def angular_velocity(self) -> int:
        ...

    @property
    @abstractmethod
    def direction_number(self) -> int:
        ...


class AbstractCommad(ABC):
    @abstractmethod
    def execute(self):
        ...


class Move(AbstractCommad):
    def __init__(self, movable: AbstractMovable) -> None:
        self.movable = movable

    def execute(self):
        self.movable.position = self.movable.position + self.movable.velocity


class Rotate(AbstractCommad):
    def __init__(self, rotatable: AbstractRotable) -> None:
        self.rotatable = rotatable

    def execute(self):
        self.rotatable.direction = (
            self.rotatable.direction + self.rotatable.angular_velocity
        ) % self.rotatable.direction_number


class MovableAdapter(AbstractMovable):
    def __init__(self, obj: Mapping) -> None:
        self.obj = obj

    @property
    def position(self) -> Vector:
        return self.obj["position"]

    @position.setter
    def position(self, new_position: Vector) -> None:
        self.obj["position"] = new_position

    @property
    def velocity(self) -> Vector:
        return self.obj["velocity"]

        # direction = self.obj["direction"]
        # direction_numbers = self.obj["directon_numbers"]
        # velocity = self.obj["velocity"]
        # new_vector = Vector(
        #     x=velocity * math.cos(2 * math.pi / direction_numbers * direction),
        #     y=velocity * math.sin(2 * math.pi / direction_numbers * direction),
        # )
        # return new_vector


class RotableAdapted(AbstractRotable):
    def __init__(self, obj: Mapping) -> None:
        self.obj = obj

    @property
    def direction(self) -> int:
        return self.obj["direction"]

    @direction.setter
    def direction(self, val: int) -> None:
        self.obj["direction"] = val

    @property
    def angular_velocity(self) -> int:
        return self.obj["angular_velocity"]

    @property
    def direction_number(self) -> int:
        return self.obj["direction_number"]
