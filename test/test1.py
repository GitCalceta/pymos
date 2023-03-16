from pymos.main import Curve, Plano
plano = Plano()
curva1 = Curve(plano,"x**2",-5,5,50)
plano.show()