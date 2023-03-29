text = input('Enter a string: ')
def func_1():
    group= tuple(text)   
    seq={}    
    for i in group:        
        if 64<ord(i)<91:
            seq['upper case:']=seq.get('upper case:',0)+1
        elif 96<ord(i)<123:
            seq['lower case:']=seq.get('lower case:',0)+1
        elif 47<ord(i)<58:
            seq['digits:']=seq.get('digits:',0)+1
        else:
            seq['others:']=seq.get('others:',0)+1
    return seq
for i in func_1().items():
    print(i[0] ,i[1])

    
    


