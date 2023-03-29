T=[{'name': 'bread', 'price': 100}, {'name': 'wine', 'price': 138}, {'name': 'meat', 'price': 15}, {'name': 'water', 'price': 1}]
print('The list of goods: {}]'.format(T))
alist=[]
n= int(input('Enter n (0<n<4): '))
for row in T:
    alist.append(row['price'])
pairs= zip(alist,T)
final=sorted(pairs,reverse=True)
i=0
result=[]
while i<n:
    result.append(final[i][1])
    i+=1
print(result)
