import random
j=0
alist=[random.randint(0,9)]
while j<11:
    blist=random.randint(0,9)
    alist.append(blist)
    j+=1
i=0
print(alist)
while i< len(alist):
    if alist.count(alist[i])==1:
        alist.pop(i)
    else:
        i+=1
print(alist)
j+=1
