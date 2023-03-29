def build_by_level(text):
    
    
    list1=text.split('\n')
    keys=[]
    texs=[]    
    print(list1)
    for i in list1:
        alist=i.split(',')
        key=alist[2]
        keys.append(int(key))
        tex=[alist[0],alist[1],alist[6]]
        tex=tuple(tex)
        list2=[]
        list2.append(tex)
        texs.append(list2)
        
    a=(list(zip(keys,texs)))
    dict1=dict(zip(keys,texs))
    print(a)
    for i in a:
        key = int(i[0])
        print(i[1])
        value=dict1.get(key)
        print(value)
        
        if not tuple(i[1]) in dict1.get(key):
           
            value.append(i[1][0])
            print(i[1])
            print()
            dict1[key]=list(set(value))
    print(dict1)
    
        
            
    
text='''1992,Andrew,5,167,14,15,49
2017,Harvey,4,132,61,—,128
2017,Irma,4,132,22,—,51'''
build_by_level(text)
        
        
        
        
        
