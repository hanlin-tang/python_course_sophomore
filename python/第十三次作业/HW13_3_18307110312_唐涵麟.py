
def func_1(text):
    
    list1=re.findall('[a-zA-Z]',text)
    string1=''.join(list1)
    list2=re.findall('[A-Z]',string1)
    flag=0
    if list1==list2:
        flag=1
    return flag

def func_2(text):
    patt=re.compile('.+!{3,}$')
    A=patt.match(text)
    flag=0
    if A!=None:
        flag=1
    return flag

def func_3(text):
    pat1=re.compile('.*\W*h+\W*e+\W*l+\W*p+\W*|a+\W*s+\W*a+\W*p+\W*|u+\W*r+\W*g+\W*e+\W*n+\W*t+\W*',re.I)
    A=pat1.match(text)
    flag=0
    if A!=None:
        flag=1
    return flag

if __name__=='__main__':
    import re
    while 1:      
        text = input('Enter an email subject:')
        if text=='':
            break
        else:
            a=func_1(text)
            
            count=func_1(text)+func_2(text)+func_3(text)
            
            if count>=1:
                print('Urgent!')

            else:
                print('Normal')
        
        
    
