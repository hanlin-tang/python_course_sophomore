def func_1(text,m):
    str1="abcdefghijklmnopqrstuvwxyz"
    result=[]
    for i in str1:
        result.append(chr((ord(i)-ord('a')+m)%26+ord('a')))
    global after
    after = ''.join(result)
    global before
    before=str1    
    table=str.maketrans(before,after)
   
    s=text.translate(table)
    return s

def func_2(secr,m):
    str2="abcdefghijklmnopqrstuvwxyz"
    table=str.maketrans(after,before)
    
    s=secr.translate(table)
    return s
    
        
    


if __name__=='__main__':
    text=input('Enter some text: ')
    m= eval(input('Enter an integer: '))
    secr=func_1(text,m)
    print('After encrypting: {}'.format(func_1(text,m)))
    print('After decrypting: {}'.format(func_2(secr,m)))
    
