x=1
y= int(input('请输入年份: '))
if y %4==0 and y %100!=0 or y % 400 == 0 :
    x=y
if x==1:
    print(bool(0))
if x-y==0:
    print(bool(1))
input('press<enter>')    
