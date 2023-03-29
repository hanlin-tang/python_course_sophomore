def func_1(a,b):
    a=a.lower()
    b=b.lower()
    alist=a.split()
    blist=b.split()
    result=[]
    for i in alist:
        if i in b :
            result.append(i)
    need= set(result)
    
    return need



if __name__=='__main__':
    a= input('Enter string1:')
    b= input('Enter string2:')
    a=list(func_1(a,b))
    b=sorted(a)
    result=','.join(b)
    print('The common words of string1 and string2: {}'.format(result))
