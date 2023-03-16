import math
class Expr():
    def __init__(self,ind,**kwargs):
        self.variables = {ind:ind}
        self.independent = ind
        if ind in kwargs:
            print('error')
        if 'x' in kwargs:
            self.variables.update({'x':kwargs['x']})
        if 'y' in kwargs:
            self.variables.update({'y':kwargs['y']})
        if 'z' in kwargs:
            self.variables.update({'z':kwargs['z']})

class Curve2D():
    def __init__(self,plano,expr,start: float,end: float,res: int):
        self.expr = expr
        self.start = start
        self.end = end
        self.res = res
        plano.add_curve(self)
    def points(self):
        delta_t = (abs(self.end-self.start))/self.res
        lista_puntos_dep = []
        for i in range(self.res+1):
            t = (i*delta_t)+self.start
            lista_puntos_dep.append(self.expr_eval(t))
        return lista_puntos_dep
        
    def expr_eval(self,value):
        values = {}
        for i in self.expr.variables:
            factor = self.expr.variables[i].replace(self.expr.independent,str(value))
            values.update({i:eval(factor)})
        return values