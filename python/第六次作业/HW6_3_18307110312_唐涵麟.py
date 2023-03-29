i=1
alist=[]
blist=[]

n=int(input('Enter a positive integer:'))     #生成要求的二维列表
blist=[x for x in range(n+1)]
for row in range(n):
    alist.append([])
    alist[row]=blist[n-i+2:]
    while i<n+1:
        alist[row].append(i)
        i+=1
    
    i=1
    n=n-1
    

for rows in alist:                     #按行输出该二维列表
    for elem in rows:
        print(elem,end='  ')
    print()

