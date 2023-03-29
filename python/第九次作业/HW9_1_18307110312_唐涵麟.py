def func(n):
    a_list=[]
    count=0
    diagmax=n+n
    dlist=[0 for i in range(n)]
    while count<n:
        a_list.append([0 for i in range(n)])
        count+=1        
    k=0  
    j=0#下三角的计数器
    for number in range(2,diagmax+1):    #按照对角线处理
        
        if number<=n+1:     #填充左上
            k+=1  #正在填充第k行对应的对角线            
            start=int((k*k-k+2)/2)
            end=int((k*k+k)/2)   #更新数据范围            
            row=k
            line=number-k  #从下到上            
            if k%2==0: #偶数列
                for keys in range(start,end+1):
                    
                    a_list[row-1][line-1]=keys
                   
                    row=row-1
                    line=line+1    #从下到上
            else:
                for keys in sorted(list(range(start,end+1)),reverse=True):
                    
                    a_list[row-1][line-1]=keys
                    
                    row=row-1
                    line=line+1 

        else:   #填充右下
            j+=1
            start=int(n*(n+1)/2+n*(j-1)-j*(j-1)/2+1)
            end=int(start+n-j-1)                       
            if n%2==0:
                if j%2==0:
                    row=n
                    line=number-n
                    for keys in range(start,end+1):                       
                       
                        a_list[row-1][line-1]=keys
                        row-=1
                        line+=1
                else:
                    row=n
                    line=number-n
                    for keys in sorted(list(range(start,end+1)),reverse=True):
                        
                        a_list[row-1][line-1]=keys
                        row-=1
                        line+=1
                        
            else:
                if j%2==0:
                    row=n
                    line=number-n
                    for keys in sorted(list(range(start,end+1)),reverse=True):
                        
                        a_list[row-1][line-1]=keys
                        row-=1
                        line+=1
                else:
                    row=n
                    line=number-n
                    for keys in range(start,end+1):
                        
                        
                        a_list[row-1][line-1]=keys
                        row-=1
                        line+=1
    return a_list

                        
if __name__=='__main__':
    n=int(input('Enter n: '))
    result=func(n)
    lenth=len(tuple('n*n'))
    for row in result:
        for line in row:
            compensate=' '*(lenth-len(tuple(str(line))))
            
            print('{}{}'.format(compensate,line),end=' ')
        print()
    




