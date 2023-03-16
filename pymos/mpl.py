import matplotlib.pyplot as plt
import math

class Plane2D():
    def __init__(self):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        self.ax.grid()
        self.ax.spines['left'].set_position('zero')
        self.ax.spines['right'].set_color('none')
        self.ax.spines['bottom'].set_position('zero')
        self.ax.spines['top'].set_color('none')
        self.curves = []
    def add_curve(self,curve):
        self.curves.append(curve)
    def show(self):
        self.render_curves()
        plt.show()
    def render_curves(self):
        for i in self.curves:
            puntos = i.points()
            x = list(map(lambda d: d['x'],puntos))
            y = list(map(lambda d: d['y'],puntos))

            self.ax.plot(x,y)
    def save(self,name):
        self.render_curves()
        plt.savefig(name)
    def flush_curves(self):
        self.curves = []