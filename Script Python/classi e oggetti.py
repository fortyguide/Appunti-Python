#Programmazione ad oggetti e Classi
class Triangle:

    #attributi della Classe
    def __init__(self, a, b, c, h):
        self.a, self.b, self.c, self.h = a, b, c, h

    #metodi della Classe
    def area(self):
        return self.b * self.h / 2
    
    def perimeter(self):
        return self.a + self.b + self.c
    

#istanzio un nuovo oggetto
triangle = Triangle(4, 3, 8, 5)

area = triangle.area()
perimeter = triangle.perimeter()

print(area)
print(perimeter)