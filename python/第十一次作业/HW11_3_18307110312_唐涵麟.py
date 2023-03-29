def func_(a):    
    
        
    alp_list=list(a)
    L=len(alp_list)
    alp_list1=alp_list[L-2:]
    last2=''.join( alp_list1)
    list1=['a','e','i','o','u']
    flag=1
    if (not alp_list[L-2] in list1) and alp_list[L-1]=='y':
        flag=0
    if a=='have':
        result='has'
    elif a=='be':
        result='is'
    
    elif alp_list[L-1]=='s' or alp_list[L-1]=='x' or alp_list[L-1]=='o' or last2=='ch' or last2=='sh':
        alp_list.append('es')
        result=''.join(alp_list)
    elif  flag==0:
        alp_list[L-1:]=['i','es']
        result=''.join(alp_list)
    else:
        alp_list.append('s')
        result=''.join(alp_list)
    return result
    




if __name__=='__main__':
    while 1:    
        a = input('Enter a verb: ')
        lenth=len(list(a))
        left=7-lenth
        space=' '*left
        if a=='q' or a=='e':
            print('Bye~~')
            break
        else:
            print('{}{}-> {}'.format(a,space,func_(a)))
            
