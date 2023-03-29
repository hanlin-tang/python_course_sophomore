def combine(list_1):
    "将列表元素合并为字符串"
    b=''
    for i in list_1:
        b = b+i
    return b
def combine1(list_1):
    "将列表元素合并为字符串,元素用空格相隔"
    b=''
    for i in list_1:        
        b=b+i+' '       
    return b
if __name__=='__main__':
    a=input('Please enter an English paragraph:\n')
    list_1=a.split()   
    for i in range(len(list_1)-1,-1,-1):       
        if list_1[i].lower()==list_1[i-1].lower():            
            list_1.pop(i)
            
    for i in range(len(list_1)-1,-1,-1):   #处理含标点重复的情况
        list_2=list(list_1[i])
        item=list_2[len(list_2)-1]
        if not (65<=ord(item)<=90 or 97<=ord(item)<=122):  #判断是否含有标点符号            
            list_2=list_2[:(len(list_2)-1)]            
            string=combine(list_2)            
            if string.lower()==list_1[i-1].lower():
                list_1[i-1:i+1]=[list_1[i-1]+item]
    
    print('After deleting consecutive identical words, the paragraph is:\n{}'.format(combine1(list_1)))
