def sanitize(time_string):
    import re
    patt1=re.compile('([0-9]{1})[\W]{1}([0-9]{2})')
    listtime=patt1.findall(time_string)
    listtime=listtime[1:]
    result = []
    for i in listtime:
        i='.'.join(i)
        result.append(i)
    return(result)
    print(result)


def get_coach_data(filename):
    import re
    with open(filename) as f:
        line=f.readline()
        name=re.findall('\\b[a-zA-Z]+\\b',line)
        name=' '.join(name)
        result=sanitize(line)   #规范后的数字列表，数字是字符
        com=[eval(i) for i in result ]        
        com=list(set(com))
        com.sort()        
        com=com[:3]
        com1=[str(i) for i in com]
        print('{}\'s fastest times are: {}'.format(name,com1))
        

if __name__=='__main__':
    #sanitize('2-34,3:21,2.34,2.45,3.01,2:01,2:01,3:10,2-22,2-01,2.01,2:16')
    get_coach_data('james.txt')
    get_coach_data('julie.txt')    
    get_coach_data('mikey.txt')
    get_coach_data('sarah.txt')
    
    
