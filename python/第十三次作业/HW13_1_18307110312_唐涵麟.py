import re
while 1:    
    a=input('Enter an email address:')
    if a=='':
        break
    if '@'in a:
        b=a.split('@')               
        patt=re.compile('[A-Za-z0-9]+(\-*|\.*|\w*)+[A-Za-z0-9]$')
        flag=patt.match(b[0])    
        b1=b[1].strip()
        pat=re.compile('[A-Za-z0-9]+\-*[A-Za-z0-9]+')
        list1=b1.split('.')
        flag2=0
        count=0
        for i in range(len(list1)-1):
            if [list1[i]]==pat.findall(list1[i]):                
                count+=1        
        pat3=re.compile('[A-Za-z]{2,3}')  
        if [list1[-1]]==pat3.findall(list1[-1]):
            count=count+1            
        if count==len(list1):
            flag2=1        
        if flag!=None and flag2==1:            
            print('valid')     
        else:
            print('invalid')
    else:
        print('invalid')
        

