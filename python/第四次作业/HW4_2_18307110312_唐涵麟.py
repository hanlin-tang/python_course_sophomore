import math
i=0
j=1
k=1
q=1
while i <4:
    thounsand=i=i+1
    while j<=4:
        hundred=j
        while k<=4:
            ten= k
            while q<=4:
                a=1000*thounsand+100*hundred+10*ten+q
                if i!=j and j!=k and k!=q and i!=k and i!=q and j!=q:                  
                    n=2
                    while n<math.sqrt(a)-1:
                        if a%n==0:
                            break
                        n+=1
                    else:
                         print(a,end=' ')
                q+=1
            q=1
            k+=1
        k=1
        j+=1
    j=1
    
        
        
        
        
            
            
