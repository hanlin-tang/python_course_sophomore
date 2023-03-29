text = input (' :')
try:
    x,y=text.split(' ')
    print(x,y)
except TypeError:
    print('gs')
