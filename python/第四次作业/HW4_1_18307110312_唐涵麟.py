'''
S1.输入三个点的坐标
S2.将三个点转化为数组
S3.提取对应的坐标
S4.利用平面坐标线段公式计算边长
S5.判断是否能构成三角形，如果不是，输出‘Three points are collinear, which can not make a triangle，是三角形则执行S6.
S6.定义变量A=B=C=0.
S7.判断是否为等腰三角形，是则定义变量A为1
S8.判断是否为直角三角形，是则定义变量B为1
S9.判断是否为等边三角形，是则定义变量C为1
S10.如果C=1，输出：’等边‘
如果B=1且A=1 ，输出：’等腰直角‘
如果B=1且A!=1,输出：’直角‘
若A=1，输出等腰，否则输出’普通‘


'''
import math
print('Enter the coordinates of 3 points: ')
alist= list(eval(input('1st point: ')))
blist=list(eval(input('2ed point: ')))
clist= list(eval(input('3rd point: ')))
a=math.sqrt((alist[0]-blist[0])*(alist[0]-blist[0])+(alist[1]-blist[1])*(alist[1]-blist[1]))
b=math.sqrt((alist[0]-clist[0])*(alist[0]-clist[0])+(alist[1]-clist[1])*(alist[1]-clist[1]))
c=math.sqrt((clist[0]-blist[0])*(clist[0]-blist[0])+(clist[1]-blist[1])*(clist[1]-blist[1]))
A=B=C=0
if not (a + b -c > 0  and abs(a-b))<c:
    print('Three points are collinear, which can','not','make a triangle')
else:
    if abs(a-b)<1e-6 or abs(a-c)<1e-6 or abs(b-c)<1e-6:
        A=1
    if abs((a*a+b*b)-c*c)<1e-6 or abs(b*b+c*c-a*a)<1e-6 or abs(a*a+c*c-b*b)<1e-6:
        B=1
    if abs(a-b)<1e-6 and abs(b-c)<1e-6:
        C=1
    if C==1:
        print('An equilateral triangle. ')
    elif B==1 and A==1:
        print('An isosceles right triangle. ')
    elif B==1 and A!=1:
        print('A right triangle.')
    elif A==1 and B!=1:
        print('An isosceles triangle.')
    else:
        print('A triangle.')

# 注意区分not 1 and 2 和not (1 and 2)
