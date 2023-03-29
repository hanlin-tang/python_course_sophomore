import math
r= eval(input('Radius? '))
s=math.pi*r**2
print('Area:', '%0.2f'% s)
print('Its integral part is a %s-digit number.'%len('%d'%s))

