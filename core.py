from typing import List, Tuple
from sympy import symbols, lambdify, sin, Symbol, Eq
import numpy as np
import matplotlib.pyplot as plt
import cProfile


class Dimension():
    def __init__(self, name: str, system: str) -> None:
        self.name = name
        self._system = None
        self.system = system

    @property
    def system(self):
        return self._system

    @system.setter
    def system(self, abreviation: str):
        match abreviation:
            case "I":
                self._system = 'imaginary'
            case "R":
                self._system = 'real'

    def __str__(self) -> str:
        return self.name+": "+self.system


class Curve():
    def __init__(self, independant: List[Symbol], eq: Eq) -> None:
        self.independant = self.dic_var(independant)
        self.eq = eq
        self.eval_eq = lambdify(independant, self.eq, np)

    def create_points(self, divisions: int, range_p: List[tuple]):
        if len(range_p) != len(self.independant):
            return False
        else:
            linspaces = []
            for i in range_p:
                linspaces.append(np.linspace(i[0], i[1],
                                             divisions, dtype=np.float32))
            grid = np.meshgrid(*linspaces)
            values = self.eval_eq(*grid)
            return *grid, values

    def dic_var(self, variables: List[Symbol]):
        dictionary = {}
        for i in variables:
            dictionary[i.name] = i
        return dictionary

    def square_points(self, center: Tuple[int], length: int):
        range_dim = []
        for i in center:
            min_ = i-length
            max_ = i+length
            range_dim.append((min_, max_))
        return self.create_points(30, range_dim)


def test():
    a, b = symbols('a b')
    eq = sin((a**2) + (b**2))
    curva = Curve([a, b], eq)
    z = curva.square_points((0, 0), 2)
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.plot_surface(z[0], z[1], z[2], edgecolor='none',
                    linewidth=0, antialiased=True, rcount=30, ccount=30)
    ax.set_aspect('equal')
    plt.show()


if __name__ == '__main__':
    import pstats
    cProfile.run('test()', 'info.dat')
    with open("time.txt", "w") as f:
        p = pstats.Stats("info.dat", stream=f)
        p.sort_stats("time").print_stats()
