##'''
##def func(L):
##    "找到L内的所有质数并返回列表"
##    list1=[]
##    for i in range (2,L+1):
##        k=2
##        while k<i:
##            if i%k==0:
##                break
##            else:
##                k+=1
##        else:
##            list1.append(i)
##    return list1
##'''
##
###A,B,L=eval(input('逗号分隔：'))
##def Reduce(A,B,L):
##    list1=[]
##    for i in range (2,L+1):
##        k=2
##        while k<i:
##            if i%k==0:
##                break
##            else:
##                k+=1
##        else:
##            list1.append(i)
##    
##    alist=[]
##    for A1 in list1:
##        
##        for B1 in list1:
##            if A1*B>A*B1:
##                alist.append([A1,B1])
##    
##    j=0
##    for item1 in alist:        
##        for item2 in alist:
##            if item1[0]*item2[1]<=item2[0]*item1[1]:
##                j+=1
##        if j==len(alist):
##            need=item1
##        else:
##            j=0
##        
##    
##        
##
##        
##    return need
##
##
##if __name__ =='__main__':
##    obj=input('输入支持人数A，反对人数B，上限L（空格分隔）：')
##    b=obj.split()
##    A=int(b[0])
##    B=int(b[1])
##    L=int(b[2])
##    
##    list_1=Reduce(A,B,L)
##    print('({} :{})约等于（{} ：{}）'.format(A,B,list_1[0],list_1[1]))
##    
  
    

def combine(list_):
    "将列表元素合并为字符串"
    b=''
    for i in list_:
        b = b+i
    return b
print(len((combine(['a','a']))))
