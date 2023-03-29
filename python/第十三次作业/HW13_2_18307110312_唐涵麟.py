import re
b=input(': ')
pet=re.compile('>(.+?)<')
a=pet.findall(b)
for i in a:
    print(i,end='')
