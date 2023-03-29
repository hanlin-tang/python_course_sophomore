a=input('Enter some text: ')
b=[x for x in a if x!=' ']
d=[b.count(c) for c in b]   # 所有字母可能的次数
for i in range(len(d)-1,-1,-1):
    if d.count(d[i])!=1:
        d.pop(i)
squ={}
for ch in b:
    squ[ch]=squ.get(ch,0)+1   #将字母和其个数连系成字典
e=[item for item in squ.items()]
alist=[]
final={}
for k in d:    
    for row in e:        
        if row[1]==k:
            alist.append(row[0])    #将所有个数相同的字符组成列表
    final[k]=alist  
    alist=[]     #更新alist为空列表
print('The "Freq-chars" dictionary is: \n {}'.format(final))           
     
            
    
