def func_1(text,m):
    result=[]
    for i in text:
        if i!=' ':
            result.append(chr((ord(i)-ord('a')+m)%26+ord('a')))
        else:
            result.append(i)
    return ''.join(result)

def func_2(secr,m):
    result=[]
    for i in secr:
        if i!=' ':
            result.append(chr((ord(i)-ord('a')-m)%26+ord('a')))
        else:
            result.append(i)
    return ''.join(result)   
            
 
if __name__=='__main__':
    text=input('Enter some text: ')
    m= eval(input('Enter an integer: '))
    secr=func_1(text,m)
    print('After encrypting: {}'.format(func_1(text,m)))
    print('After decrypting: {}'.format(func_2(secr,m)))
