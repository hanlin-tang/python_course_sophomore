import random
j=0
alist=[random.randint(1,19)]
while j<19:
    blist=random.randint(1,19)
    alist.append(blist)
    j+=1

ran=alist[:]    #利用切片保存初始列表的值,注意用赋值会导致ran列表一同变化。

for i in range(len(alist)-1,-1,-1):
    if alist.count(alist[i])!=1:
        del alist[i]

left=alist         #倒序删除重复元素可不改变原列表顺序

print('Using while:')  # while  

m=0
even=[]
odd=[]
while m<len(alist):
    if alist[m]%2==0:
        even.append(alist[m])
    else:
        odd.append(alist[m])
    m+=1

   
print('20 random integers are: {}'.format(ran))
print('Among them, the odd numbers are : {}'.format(odd))
print('And the even numbers are : {}'.format(even))



j=0                                   # for
alist=[random.randint(1,19)]
while j<19:
    blist=random.randint(1,19)
    alist.append(blist)
    j+=1
i=0
ran=alist[:]
for i in range(len(alist)-1,-1,-1):
    if alist.count(alist[i])!=1:
        del alist[i]
left=alist         #倒序删除重复元素可不改变原列表顺序
even=[]
odd=[]
for k in alist:
    if k%2==0:
        even.append(k)
    else:
        odd.append(k)
print('Using for:')
print('20 random integers are: {}'.format(ran))
print('Among them, the odd numbers are : {}'.format(odd))
print('And the even numbers are : {}'.format(even))

j=0   #  list comprehensions
alist=[random.randint(1,19)]
while j<19:
    blist=random.randint(1,19)
    alist.append(blist)
    j+=1
ran=alist[:]

for i in range(len(alist)-1,-1,-1):
    if alist.count(alist[i])!=1:
        del alist[i]

left=alist         #倒序删除重复元素可不改变原列表顺序

even=[x for x in left if x%2==0]
odd=[x for x in left if x%2!=0]
print('Using list comprehensions:')
print('20 random integers are: {}'.format(ran))
print('Among them, the odd numbers are : {}'.format(odd))
print('And the even numbers are : {}'.format(even))


