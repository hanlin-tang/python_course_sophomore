a=input('Please enter your first name: ')
print('Hi,',a,'!')
mid,fin=eval(input('Please enter your midterm and final exam grades (separated with comma): '))
c=list(eval(input('Enter all your homework grades(separated with comma):')))
c.sort()
d=len(c)
if len(c)%2==0:
    H=(c[int(d/2-1)]+c[int(d/2)])/2
else:
    H=c[int((d-1)/2)]
print('Your homework grade is: {}'.format(H))
T=0.2*mid+0.4*fin+0.4*H
print(0.2*mid,0.4*fin,0.4*H)
print('Your final grade is: {:.6}'.format(T))
