import numpy as np


def four_petal_rose(a: int, angle: float) -> float:
    return a * np.sin(2*angle)


def three_petal_rose(a: int, angle: float) -> float:
    return a * np.sin(3*angle)


def logarithmic_spiral(a: int, angle: float) -> float:
    return np.exp(a * angle)


def hyperbolic_spiral(a: int, angle: float) -> float:
    return a / angle


def archimede_spiral(a: int, angle: float) -> float:
    return a * angle


def cardiode(a: int, angle: float) -> float:
    return a * (1 + np.cos(angle))
