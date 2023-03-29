import random
a=[random.randint(0,99) for i in range(1000)]
b={}
print('The random list is: \n {} '.format(a))
print()
k=sorted(a)
print('The statistical result is: ')
for key in k:
    b[key]=b.get(key,0)+1
j=0
for m,n in b.items():
    if (m<10 and n<10) :
        print('( {}:  {})'.format(m,n),end=' ')
    elif (m<10 and n>=10):
        print('( {}: {})'.format(m,n),end=' ')
    elif (m>=10 and n<10):    
        print('({}:  {})'.format(m,n),end=' ')
    else:
        print('({}: {})'.format(m,n),end=' ')        
    j+=1
    if j%10==0:
        print()
        
    
