import random
def sort(iterable,reverse=False):
    "输入可迭代对象，输出默认升序后结果"
    p=list(iterable)   #将所有的迭代对象转化为列表
    n=len(p)
    if not reverse:
        q=p[:]
        k=0
        while k<n-1:
            index_min=k
            for i in range(k,n):
                if p[i] < p[k]:
                    index_min=i
                    p[k]=p[i]      #找出最小值下标并赋值给第一个元素
            p[k]=q[k]#恢复原列表             
                      
            a=p[k]          
            b=p[index_min]
           
            p[k],p[index_min]=b,a
            k+=1
            
            q=p[:]
    else:
        q=p[:]
        k=0
        while k<n-1:
            index_max=k
            for i in range(k,n):
                if p[i] > p[k]:
                    index_max=i
                    p[k]=p[i]
            
            p[k]=q[k]#恢复原列表               
                      
            a=p[k]
          
            b=p[index_max]
           
            p[k],p[index_max]=b,a
            k+=1
            
            q=p[:]  #保存一次迭代后的列表
    return p


if __name__=='__main__':
    ranlist=[]

    for i in range(10):
        need=random.randint(1,100)
        ranlist.append(need)
    print('The testing list is: ')
    print(ranlist)
    print('After calling the function "sort(test_list)", the return list is:')
    print(sort(ranlist))
    print('After calling the function "sort(test_list,reverse=True)", the return list is:')
    print(sort(ranlist,reverse=True))
    print()
    
    dic1={}
    for j in range(10):
        
        if random.randint(0,1)==0:   #随机生成大写或小写字母
            key=chr(random.randint(65,90))
        else:
            key=chr(random.randint(97,122))
        value=random.randint(1,100)
        item={key:value}
        dic1.update(item)
    print('The testing dict is: ')
    print(dic1)
    print('After calling the function "sort(test_dict)", the return list is:')
    print(sort(dic1))
    print('After calling the function "sort(test_dict,reverse=True)", the return list is:')
    print(sort(dic1,reverse=True))
