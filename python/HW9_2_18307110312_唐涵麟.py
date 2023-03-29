def func(choice,n=1):
    T=[{'name': 'bread', 'price': 100}, {'name': 'wine', 'price': 138}, {'name': 'meat', 'price': 15}, {'name': 'water', 'price': 1}]    
    t=[{'name': 'pen', 'price': 5}, {'name': 'whiteboard', 'price': 170}, {'name': 'pencil', 'price': 1}]
    alist=[]
    if choice==1:
        
        final=sorted(T, key=lambda x: x['price'] ,reverse=True)               
        i=0
        result=[]
        while i<n:
            result.append(final[i])
            i+=1
    else:
        final=sorted(t, key=lambda x: x['price'] ,reverse=True)
        i=0
        result=[]
        while i<n:
            result.append(final[i])
            i+=1
    return result 

if __name__=='__main__':
    print(func(1,2))
    print(func(0))
