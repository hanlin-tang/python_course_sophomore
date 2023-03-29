'''
text = input('Enter a file: ')
group= tuple(text)
seq={}
for i in group:
    if 64<ord(i)<91:
        seq['upper']=seq.get('upper',0)+1
    elif 96<ord(i)<123:
        seq['lower']=seq.get('lower',0)+1
    elif 47<ord(i)<58:
        seq['number']=seq.get('number',0)+1
    else:
        seq['others']=seq.get('others',0)+1
print(seq)
'''
'''
text = input('Enter a file: ')
group= tuple(text)
seq={}
for i in group:    
    if 64<ord(i)<91:
        seq['upper']=seq.get('upper',0)+1
    elif 96<ord(i)<123:
        seq['lower']=seq.get('lower',0)+1
    elif 47<ord(i)<58:
        seq['number']=seq.get('number',0)+1
    else:
        seq['others']=seq.get('others',0)+1
print(seq)

'''
text = input('Enter a file: ')
group= tuple(text)   
seq={}

for i in group:        
    if 64<ord(i)<91:
        seq['upper']=seq.get('upper',0)+1
    elif 96<ord(i)<123:
        seq['lower']=seq.get('lower',0)+1
    elif 47<ord(i)<58:
        seq['number']=seq.get('number',0)+1
    else:
        seq['others']=seq.get('others',0)+1
    


