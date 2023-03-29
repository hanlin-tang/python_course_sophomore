import math
x= input ('输入两边长夹角：')
a,b,sita = eval(x)
c=math.sqrt(a**2+b**2-2*a*b*math.cos(math.radians (sita)))
print(c)
