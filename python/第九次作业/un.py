'''
p=[2,-399,2,3,5,6,-78,1]
n=len(p)
index_min=1
for i in range(1,n):
    if p[i] < p[1]:
        index_min=i
        p[1]=p[i]
print(index_min)
'''
##import random
##dict1={}
##for j in range(10):    
##    key=chr(random.randint(65,122))
##    value=random.randint(1,100)
##    item={key:value}
##    dict1.update(item)
##print(dict1)

for i in range(65,122):
    print(chr(i))
