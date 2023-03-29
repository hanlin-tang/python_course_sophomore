import math
r= eval(input('Radius? '))
s=math.pi*r**2
print('Area: ', '%0.2f'% s)
b=int(s)
c=str(b)
m=len(c)
print('Its integral part is a ',m,'-digit number.',sep='')

