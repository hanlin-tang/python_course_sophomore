def func(choice,n=1):
    T=[{'name': 'bread', 'price': 100}, {'name': 'wine', 'price': 138}, {'name': 'meat', 'price': 15}, {'name': 'water', 'price': 1}]    
    t=[{'name': 'pen', 'price': 5}, {'name': 'whiteboard', 'price': 170}, {'name': 'pencil', 'price': 1}]
    alist=[]
    if choice==1:
        for row in T:
            alist.append(row['price'])
        pairs= zip(alist,T)
        final=sorted(pairs,reverse=True)
        i=0
        result=[]
        while i<n:
            result.append(final[i][1])
            i+=1
    else:
        for row in t:
            alist.append(row['price'])
        pairs= zip(alist,t)
        final=sorted(pairs,reverse=True)
        i=0
        result=[]
        while i<n:
            result.append(final[i][1])
            i+=1
    return result 

if __name__=='__main__':
    print(func(1,2))
    print(func(0))
