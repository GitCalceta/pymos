from pymos.main import Curve2D, Expr
from pymos.mpl import Plane2D
plano = Plane2D()

expr = Expr('{t}', x='math.cos({t})*(math.sin({t})+1)', y='math.sin({t})*(math.sin({t})+1)')
curva1 = Curve2D(plano,expr,-0,10,200)
plano.show()