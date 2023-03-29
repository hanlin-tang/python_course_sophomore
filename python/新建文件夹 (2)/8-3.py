r='='*23
print('{}Bulls and Cows{}'.format(r,r))
print()
print('Instruction: Please guess a number between 1 and 100. You have 5 chances.')
print()
import random
a=random.randint(1,100)
i=0
corre=[1]
def guess(m):
    "输入m,判断其与随机数的大小关系并输出相应值"    
    if m==a:
        print('Yeh!:D', end = ' ')
        corre[0]=2
       
    elif m>a:
        print('bigger',end = '.')
    else:
        print('Smaller',end = '.')

while i<5:             
    m= int(input('Guess: '))
    guess(m)
    if corre[0]==2:
        break
    i+=1
    print(' {} chances left'.format(5-i))
else:
    print("Oops...It's {}. Good luck next time!".format(a))


input('press<Enter>')
