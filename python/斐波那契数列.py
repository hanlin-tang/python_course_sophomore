a=0
b=1
i=1
s=0
n=int(input(' :'))
while i<=n:
    a,b=b,a+b
    i+=1
    s=s+a
    print(a,end=' ')
print(s)
    
