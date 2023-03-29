i=1
b=1
s=1
x=float(input('Enter a number: '))
while 1:
    s=s*x/i
    b=b+s
    i=i+1
    if abs(s)<10**(-10):
        break
print('e**{} = {}'.format(x,b))
