while True:
    s=a=int(input('Enter a positive integer: '))
    if s==0:
        break #s 为0 的时候跳出循环
    print(s,'= ',end='')  
    i=2
    while 1:
        if a==1 :
            print(a)
            break  # 1作为特殊值单独考虑
        if a%i==0:
            print(i,end='\n')
            a=a/i
            break
        else:
            i+=1   # 整个语句块用于输出最小因子
            
    found = False     
    while 1 :  
        if a==1:   
            break  
        
        if a%i==0: 
            print ('*',i,end=' ')
            a=a/i
            if a%i==0:
                continue 
            n=a     
            j=2
            while j< n:
                if n%j==0:
                    break  
                j+=1
            else:
                found =True  
        else:
            i+=1
        if found:
            break   
    if a!=1:
        print('*',int(a))  # 输出最后结果

input('press<Enter>')    
'''S1.输入s的值
S2.2=>i（i作为除数）
S3.s被i除，若能够整除，则输出i(作为s的一个因子)，a=a/i,否则执行S5
S4.重复S3直到a不整除i
S5.判断a是否为质数，是则跳出循环，结束,否则执行S6
S6.i=>i+1
S7.回到S3'''
