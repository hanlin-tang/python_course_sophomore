##'''x = [1, 2, 1, 2, 1, 1, 1]
##while 1:
##    x.remove(1)
##    if x.count(1)==0:
##        break
##print(x)
##
##a=[]
##for i in range(4):
##    a.append([])
##    for j in range (4):
##        item=input('Num:')
##        a[i].append(item)
##print(a)
### 创建二维矩阵
##
##from collections import defaultdict
##a=defaultdict(int)
##
##a={}
##for i in 'asdjf, asdf, asdfjjejg,daf':
##    a[i]+=1
##print(a)
##
##'''
##with open('try.txt') as f:
##    list0=[i.strip() for i in f]
##    list1=[i for i in list0 if not i.startswith('#')]
##    list1= [ str(i)+j+'\n' for i,j in enumerate(list1,1)]
##    for i in list1:
##        i+='\n'
##with open('try_n.txt','w') as f:
##    f.writelines(list1)
##'''
##
##
##'''
##def sum(n):
##    assert(n>=0),"N must be greater than 0"
##    r=0
##    for i in range(1,n+1):
##        r+=i
##    return r
##try:
##    n=int(input('enter:'))
##    print(sum(n))
##except AssertionError as reason:
##    print(reason)
##    

a_list = ['China', 'America', 'England', 'France']
while True:
    n = int(input('请输入字符串的序号(0~3): '))
    try:
        print(a_list[n])
    except IndexError as err:
        print(err)
    else:
        break
