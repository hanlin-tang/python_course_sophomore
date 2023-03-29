a=[1,1,2,3,4,5,6,7,8,99,9,9,9,9,9,10]
for i in range(len(a)-1,-1,-1):
    print(range(len(a)-1,-1,-1))
    if a[i]%2!=0:
        a.pop(i)
print(a)
