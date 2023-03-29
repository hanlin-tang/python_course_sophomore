####num = 1
####found= False 
####while not found: #
####    if num%3==2 and num%5==3 and num%7==4:
####        found= True
####    else:
####        num+=1
####print (num)


##num =1
##while True :
##    if num%3==2 and num%5==3 and num%7==4:
##        break
##    else:
##        num+=1
##print(num)


##num = 1
##found= False
##count=0
##n=int(input('输入个数： '))
##while count < n:
##    while not found: 
##        if num%3==2 and num%5==3 and num%7==4:
##            found= True
##        else:
##            num+=1
##    else:
##        print(num)
##        count+=1
##        num+=1
##        found =False


##num = 1
##found= False
##count=0
##n=int(input('输入个数： '))
##while count < n:
##    while 1: 
##        if num%3==2 and num%5==3 and num%7==4:
##            print(num)
##            break
##        else:
##            num+=1
##    count+=1
##    num+=1     # 如何扫描多个符合条件的数值


num=1
i=0
n=int(input('输入个数： '))
while i<n :
    if num%3==2 and num%5==3 and num%7==4:
        print(num)
        i=i+1
        num+=1
    else:
        num+=1
