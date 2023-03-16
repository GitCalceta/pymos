import matplotlib.pyplot as plt

class Curve():
    def __init__(self,plano,expr,start,end,res):
        self.expr = expr
        self.start = start
        self.end = end
        self.res = res
        plano.add_curve(self)
    def points(self):
        delta_x = (abs(self.end-self.start))/self.res
        lista_puntos_x = []
        lista_puntos_y = []
        for i in range(self.res+1):
            x = (i*delta_x)+self.start
            lista_puntos_x.append(x)
            lista_puntos_y.append(self.expr_eval(x))
        return [lista_puntos_x,lista_puntos_y]
        
    def expr_eval(self,value):
        x = value
        return eval(self.expr)

#Saca los promedios de los valores
def razon_de_cambio(puntos):
    razones_list = [puntos[1]-puntos[0]]
    for i in range(len(puntos)-1):
        razon = puntos[i+1]-puntos[i]
        razones_list.append(razon)
    return razones_list


class Plano():
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
            self.ax.plot(puntos[0],puntos[1])
    def save(self,name):
        self.render_curves()
        plt.savefig(name)
    def flush_curves(self):
        self.curves = []