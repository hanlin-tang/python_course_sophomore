for x in range(10,100000):
    i=0
    X=str(x)
    X=tuple(X)
    lenth=len(X)    
    while i<lenth-1:
        a=X[i]
        k=i-1
        while k>=0:

            a=X[k]+a
            k-=1
        j=1
        b=X[i+1]
        while j<(lenth-i-1):
            b=b+X[i+j+1]            
            j+=1
        
        A=int(a)
        B=int(b)
        if (A+B)*(A+B)==x:
            print('{}=({}+{})**2'.format(x,A,B))
        i+=1
            

        
