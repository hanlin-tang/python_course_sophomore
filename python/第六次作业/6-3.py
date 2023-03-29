
import random
j=0
alist=[random.randint(1,19)]
while j<19:
    blist=random.randint(1,19)
    alist.append(blist)
    j+=1

ran=alist[:]    #利用切片保存初始列表的值,注意用赋值会导致ran列表一同变化。

for i in range(len(alist)-1,-1,-1):
    if alist.count[alist[i]]!=1:
        del alist[i]
