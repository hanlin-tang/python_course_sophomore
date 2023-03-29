def dic(fname):
    with open(fname) as f:
        alist=f.readline().split(',')
    return alist

def gener(dic1,a):
    import random
    
    i=0
    while i<a:
        adj=random.choice(dic1['adj'])
        noun=random.choice(dic1['noun'])
        verb=random.choice(dic1['verb'])
        st=str(i+1)
        print(st.rjust(len(str(a))),end='') #标号右对齐
        print('.The {} {} {}.'.format(adj,noun,verb))
        i+=1
    
        
    
if __name__=='__main__':
    dic1={}
    
    dic1['adj']=dic('adj.txt')
    dic1['noun']=dic('noun.txt')
    dic1['verb']=dic('verb.txt')
    
    while 1:
        try:
            a=int(input('请输入需要创建的句子数目:'))
        except ValueError:
            print('输入有误，重新输入...')
        else:
            break
    gener(dic1,a)
    
        
