def ana(fname):
    import re
    with open(fname) as f:
        lineslist=f.readlines()
    patt=re.compile('([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})')
    patt2=re.compile('\\b([a-z.]+)\\b')
    dic={}
    for i in lineslist:
        i=i.strip()        
        if not i.startswith('#') and 'ignore' not in i:
            a=patt.findall(i)
            if '#' in i:
                i=re.findall('(.+)#',i)
                i=i[0]            
            b=patt2.findall(i)            
            b2=b[3:]
            for item in b2:
                
                dic.setdefault(a[0],[]).append(item)            
    print('The dict is: {}'.format(dic))


if __name__=='__main__':
    ana('hosts')
    




