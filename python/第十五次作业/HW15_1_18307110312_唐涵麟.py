def find_mag(x,y):
    result=0
    global flag
    flag=1    
    try:
        c=x+y
        import math
        math.sqrt(y-x)
        for i in range(x,y+1):
            a=str(i)            
            listnum2=[int(j) for j in a if j!='0']            
            count=0
            for j in listnum2:
                if i%j==0:
                    count+=1
            if count== len(listnum2):
                result+=1
        print('[{},{}] has {} magic numbers!'.format(x,y,result))      
    except ValueError:
        print('wrong range')

    except TypeError:
        print('wrong type!')
    else:        
        flag=0        
    return result


if __name__=='__main__':    
    contin='y'
    while 1:
        if contin=='n':
            print('Bye....')
            break
        flag1=1
        while 1:
            try:
                text=input('Please enter range[a,b](0<a<=b):')
                import re        

                x,y=re.split('-| |,',text)
                try:
                    x=int(x)
                    y=int(y)
                except Exception:
                    pass                                
                
                find_mag(x,y)                       
            
            except (ValueError):
                print('wrong separator!')
            else:
                flag1=0                
            if flag1==0 and flag==0:
                break
        contin=input('Continue? (Y/N)')
    
       

            
