import math

eq = '4x^2 +4x +    (-8) =   0'
a = int(eq.split('x^2')[0])
b = int(eq.split('x^2')[1].split('x')[0].strip())
c = int(eq.split('+')[-1].split('=')[0].strip().replace('(', '').replace(')', ''))

print (a, b, c)

x1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
x2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)

print(x1, x2) 