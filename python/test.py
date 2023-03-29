'''n=100
while n>0:
    i=2
    while i<n:
        if n%i==0:
            break
        i+=1
    else:
        print(n)
        break
    n-=1
    
'''
alist=[]
for i in range(5):
    for j in range(4):
        for q in range(3):
            alist.append([i,j,q])


print(alist)
for i in alist:
    print(i)
            
