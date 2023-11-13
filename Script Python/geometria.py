class Triangolo:
     
    """Una semplice classe che calcola le misure di un triangolo"""

    def __init__(self, a, b, c, h):
          
          self.a, self.b, self.c, self.h = a, b, c, h

    def area(self):
        
        """Calcolo l'area del triangolo"""

        return float(self.b) * float(self.h) / 2
    
    def perimetro(self):
         
        """Calcolo il perimetro del triangolo"""

        return self.a + self.b + self.c
    


class Quadrato:
     
    """Una semplice classe che calcola le misure di un quadrato"""

    def __init__(self, l):
          
          self.l = l

    def area(self):
        
        """Calcolo l'area del quadrato"""

        return self.l ** 2
    
    def perimetro(self):
         
        """Calcolo il perimetro del quadrato"""

        return self.l * 4
    

class Rettangolo:
     
    """Una semplice classe che calcola le misure di un rettangolo"""

    def __init__(self, b, h):
          
          self.b, self.h = b, h

    def area(self):
        
        """Calcolo l'area del rettangolo"""

        return self.b * self.h
    
    def perimetro(self):
         
        """Calcolo il perimetro del rettangolo"""

        return 2 * (self.b + self.h)

