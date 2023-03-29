def build_by_level(text):       
    list1=text.split('\n')
    keys=[]
    texs=[]  
    
    for i in list1:
        alist=i.split(',')
        key=alist[2]
        keys.append(int(key))
        tex=[int(alist[0]),alist[1],int(alist[6])]
        tex=tuple(tex)
        list2=[]
        list2.append(tex)
        texs.append(list2)        
    a=(list(zip(keys,texs)))


    a.sort(key=lambda x:x[0],reverse=True)
    dict1=dict(a)
    
    for i in a:
        key = int(i[0])
       
        value=dict1.get(key)
             
        if not tuple(i[1]) in dict1.get(key):           
            value.append(i[1][0])
           
            m=list(set(value))
           
            m.sort(key=lambda x : x[2],reverse=True)
            dict1[key]=m            
    return dict1

            
def topn_by_level(dict_hurricanes,n=3):
    
    list2=[]
    for item in dict_hurricanes.items():
        total=0
        for each in item[1]:
            total=total+int(each[2])
        itemlist=[item[0],total,item[1]]
        list2.append(tuple(itemlist))
     #print(list2)
    list2.sort(key=lambda x:(x[1],-x[0]),reverse=True)
    final=list2[:n]
    
    return final



def print_hurricane(levels):
    for i in levels:
        total=len(i[2])
        AVG=i[1]/total
        print('Level:{} total:{} AVG:{} Total loss:{}'.format(i[0],total,AVG,i[1]),end=' ')
        for j in i[2]:
            if int(j[2])>AVG:
                print(j,end='')
        print()                  
            
      
if __name__=='__main__':        
    
    hurricanes= '''1985,Juan,1,86,18,—,4
    1992,Andrew,5,167,14,15,49
    1989,Hugo,4,138,10,14,19
    1996,Fran,3,115,16,12,8
    1999,Floyd,2,104,24,13,10
    2002,Lili,1,92,8,14,2
    2004,Charley,4,150,10,17,22
    2004,Ivan,3,121,17,13,28
    2004,Jeanne,3,121,12,8,10
    2004,Frances,2,104,24,11,13
    2005,Katrina,3,127,16,10,65
    2008,Ike,2,109,18,13,36
    2011,Irene,1,86,22,12,15
    2012,Isaac,1,81,27,7,3
    2012,Sandy,1,75,13,14,72
    2016,Matthew,2,98,19,—,11
    2017,Harvey,4,132,61,—,28
    2017,Irma,4,132,22,—,51'''
    hur_dict = build_by_level(hurricanes)
    hur_list = topn_by_level(hur_dict)
    print_hurricane(hur_list)                      #函数调用1

    print()
    hur_dict = build_by_level(hurricanes)
    hur_list = topn_by_level(hur_dict, 1)
    print_hurricane(hur_list)              #函数调用2
