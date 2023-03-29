a = input ('Enter your name: ')
b= 'Hi, %s!' % a
c='{}'.format('*'*(len(b)+4))
print(c)
print('*{}*'.format(' '*(len(b)+2)))
print('* {} *'.format(b))
print('*{}*'.format(' '*(len(b)+2)))
print(c)
input ('Press <Enter>')
