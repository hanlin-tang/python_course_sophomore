##def combine(list_1):
##    "将列表元素合并为字符串"
##    b=''
##    for i in list_1:
##        b = b+i
##    return b
##
##def combine1(list_1):
##    "将列表元素合并为字符串1"
##    b=''
##    for i in list_1:
##        if i !=list_1[len(list_1)-1]:
##            b = b+' '+i
##        else:
##            b = b+i
##    return b
##
##if __name__=='__main__':
##    a=input('text:')
##    list_1=a.split()
##    #print(list_1)
##
##    for i in range(len(list_1)-1,-1,-1):
##       
##        if list_1[i]==list_1[i-1]:
##            
##            list_1.pop(i)
##    b=combine1(list_1)
##    b=b.split()
##   
##
##    for i in range(len(list_1)-1,-1,-1):   #处理含标点重复的情况
##        list_2=list(list_1[i])
##        item=list_2[len(list_2)-1]
##        if not (65<=ord(item)<=90 or 97<=ord(item)<=122):  #判断是否含有标点符号
##            print(item)
##            print(list_2)
##           
##            list_2=list_2[:(len(list_2)-1)]
##            print(list_2)
##            string=combine(list_2)
##            print(string,list_1[i-1],1)
##            if string==list_1[i-1]:
##                list_1[i:i+1]=[item]                
##    print(list_1) 
##   
##    print(combine1(list_1))
## 
##'''
##    for i in range(len(list_1)-1,-1,-1): #处理短句开头重复的情况
##        list_2=list(list_1[i])
##        item=list_2[0]
##        if not (65<=ord(item)<=90 or 97<=ord(item)<=122):  #判断开头是否含有标点符号
##            print(item)
##            print(list_2)
##            list_2=list_2[1:]
##            print(list_2)
##            string=combine(list_2)
##            print('i:',i)
##            
##            print(string,list_1[i+1])
##            if string==list_1[i+1]:
##                list_1.pop(i+1)
##                print('yes')
##'''
##
def combine1(list_1):
    "将列表元素合并为字符串,元素用空格相隔"
    b=''
    for i in list_1:        
        b=b+i+' '       
    return b

print(combine1(['I', 'love', 'you', 'o.']))
    
