n=a= int(input('Enter a positive integer: '))  #输入s的值
print(n,'= ',end='')  
i=2
while 1:
    if a==1 :
        print(a)
        break  # 1作为特殊值单独考虑
    if a%i==0:
        print(i,end='')
        a=a/i
        break
    else:
        i+=1   # 整个语句块用于输出最小因子
while i<n:
    if a%i==0:
        print(' *',i,end='')
        a=a/i
        continue
    else:
        i+=1

'''
S1.输入s的值
S2. 判断是否为1，是则直接输出，否则进行下一步
S3. 用i除a余r ,r=0,输出i,否则运行S5
S4. a=a/i,重复S3
S5. i=>i+1
S6. 如果i<n ，返回S3；否则结束
'''

