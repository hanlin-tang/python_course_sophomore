i=1
while i< 10:
    j=1
    while j<=i:
        print('{}*{}={}'.format(i,j,i*j),end='\t')
        j+=1
    print()# 利用print函数的默认以换行结束
    i+=1
