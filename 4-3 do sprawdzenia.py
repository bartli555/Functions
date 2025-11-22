###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
#
import math

def triangle_area(a,b,c):
    s = (a + b + c) / 2 #połowa obwodu trójkąta
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area


a = int(input('Podaj bok a: '))
b = int(input('Podaj bok b: '))
c = int(input('Podaj bok c: '))

wynik = triangle_area(a,b,c)

print(f'The area of ​​a triangle with sides {a}, {b}, {c} is {wynik:.0f}')
