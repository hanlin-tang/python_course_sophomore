import math
a,b,c=eval(input('用逗号隔开的三个数字：'))
if a+b>c and abs(a-b)<c:
    s=(a+b+c)/2
    A=math.sqrt(s*(s-a)*(s-b)*(s-c))
    print(A)
else:
    print('error')
