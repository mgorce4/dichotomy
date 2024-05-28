from math import sqrt
from typing import Callable


def dicho(f: Callable[[float], float], a: float, b: float, e: float) -> float:
    while (b - a) > e:
        m = (a + b) / 2
        if f(a) * f(m) <= 0:
            b = m
        else:
            a = m

    return (a + b) / 2


def tangente(f: Callable[[float], float], fprime: Callable[[float], float], x0: float, n: int) -> float:
    x = x0
    for _ in range(n):
        x = x - f(x) / fprime(x)

    return x


def tangente_opti(f: Callable[[float], float], x0: float, n: int) -> float:
    x = x0
    for _ in range(n):
        x = f(x)

    return x

print("-------------------------------------")
print("Dichotomie:")
print(f"dicho(2)={dicho(lambda x: x**2 - 2, 0, 2, 0.0001)}, sqrt(2)={sqrt(2)}")
print(f"dicho(3)={dicho(lambda x: x**2 - 3, 0, 2, 0.0001)}, sqrt(3)={sqrt(3)}\n")
print("-------------------------------------")
print("Tangente:")
print(f"tangente(2)={tangente(lambda x: x**2 - 2, lambda x: 2 * x, 1, 5)}, sqrt(2)={sqrt(2)}")
print(f"tangente(3)={tangente(lambda x: x**2 - 3, lambda x: 2 * x, 1, 5)}, sqrt(3)={sqrt(3)}")
print()
print("-------------------------------------")
print("Tangente opti:")
print(f"tangente(2)={tangente_opti(lambda x: 1/2 * x + 1 / x, 1, 5)}, sqrt(2)={sqrt(2)}")