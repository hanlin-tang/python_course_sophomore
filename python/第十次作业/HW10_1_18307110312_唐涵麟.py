def find_1(a,b):
    "找到最大公约数"
    if a<b:
        a,b=b,a    
    while 1:
        r=a%b
        
        if r==0:
            result=b
            break
        a,b=b,r
    return result
           
def Reduce(A,B,L):
    list1=[]
    for i in range (1,L+1):
        for j in range(1,L+1):
            if find_1(i,j)==1:
                list1.append([i,j])  #找到所有L以内的所有的互质的数组成二维列表
    
    alist=[]
    for item in list1:
        A1=item[0]
        B1=item[1]
        
        
        if A1*B>A*B1:
            alist.append([A1,B1])
    
    j=0
    for item1 in alist:        
        for item2 in alist:
            if item1[0]*item2[1]<=item2[0]*item1[1]:
                j+=1
        if j==len(alist):
            need=item1
        else:
            j=0
    return need


if __name__ =='__main__':
    obj=input('输入支持人数A，反对人数B，上限L（以空格分隔）：')
    b=obj.split()
    A=int(b[0])
    B=int(b[1])
    L=int(b[2])
    
    list_1=Reduce(A,B,L)
    print('({} :{})约等于（{} ：{}）'.format(A,B,list_1[0],list_1[1]))
    

