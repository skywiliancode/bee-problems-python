import math

A, B, C = input().split()
PI = 3.14159

area_triangle_right = float(A) * float(C) / 2
area_circle = PI * math.pow(float(C), 2)
area_trapeze = (float(A) + float(B)) * float(C) / 2
area_square = float(B) * float(B)
area_right = float(A) * float(B)

print('TRIANGULO: {:.3f}'.format(area_triangle_right))
print('CIRCULO: {:.3f}'.format(area_circle))
print('TRAPEZIO: {:.3f}'.format(area_trapeze))
print('QUADRADO: {:.3f}'.format(area_square))
print('RETANGULO: {:.3f}'.format(area_right))
