def comment(fname):
    with open(fname,encoding='UTF-8') as f:
        j=1
        lines=[]
        for line in f:            
                        
            if len(line)!=1 and not line.startswith('#'):
         
                item=str(j)+')'+line
                lines.append(item)
                j=j+1
            else:
                lines.append(line)
                                   
    with open(fname[:-3]+'_n'+fname[-3:],'w',encoding='UTF-8') as f :
        f.writelines(lines)

def comment2(fname):
    with open(fname,encoding='UTF-8') as f:
        j=1
        lines=[]
        for line in f:
                      
            if len(line)!=1 and not line.startswith('//'):         
                item=str(j)+')'+line
                lines.append(item)
                j=j+1
            else:
                lines.append(line)                                   
    with open(fname[:-4]+'_n.cpp','w',encoding='cp936') as f :
        f.writelines(lines)

    
if __name__=='__main__':
    comment('property.py')
    comment2('Goldbach.cpp')
        
