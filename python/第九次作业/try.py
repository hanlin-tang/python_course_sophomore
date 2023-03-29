##n=4
##a_list=[]
##count=0
##diagmax=n+n
##dlist=[i for i in range(n)]
##
##while count<n:
##    a_list.append(dlist)
##    count+=1
##
##dig=0
##for number in range(2,diagmax+1):
##    dig+=1
##    if number%2==0:
##        k=dig           
##        start=int((dig*dig-dig+2)/2)
##        end=int((dig*dig+dig)/2)
##        print(number,'num')
##        
##        
##        if dig%2!=0:
##            j=1
##            for keys in range(start,end+1):
##                print(list(range(start,end+1)))
##                               
##                row=j
##                line=number-j
##                print(row,line,'keys',keys,a_list)
##
##               
##                j+=1
##        elif dig%2==0:
##            j=1
##            for keys in range(start,end+1):
##                print(list(range(start,end+1)))
##                               
##                row=j
##                line=number-j
##                print(row,line,'keys',keys)
##
##                a_list[line-1][row-1]=keys
##                j+=1
####
####print(a_list)
##n=4
##count=0
##a_list=[]
##dlist=[0 for i in range(n)]
##while count<n:
##    a_list.append(dlist)
##    count+=1
##k=2
##row=k
##line=3-k
##start=int((k*k-k+2)/2)
##end=int((k*k+k)/2)   #更新数据范围
##print(start,end)
##for keys in range(start,end+1):
##    a_list[row-1][line-1]=keys
##    print(row-1)
##    print()
##    print(row,line,keys,a_list,'jhjk','fini')
##    row-=1

'''      #从下到上
alist=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
i=1
row=4
line=1
for k in range(1,5):
   
    alist[row-1][line-1]=k
    row=row-1
    line=line+1
    print(alist)
print(alist)
'''
n=4
dlist=[0 for i in range(n)]
count=0
a_list=[]
while count<n:
    a_list.append(dlist)
    count+=1
a_list[0][0]=1
print(a_list)


