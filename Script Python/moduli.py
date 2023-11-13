#I moduli
#/lib/site-packages

import script

script.hello_world()

import geometria

quadrato = geometria.Quadrato(2)
print(quadrato.area())

from geometria import Triangolo, Quadrato, Rettangolo
triangolo = Triangolo(3,4,5,7)
print(triangolo.area())
print(triangolo.perimetro())



