import random
list1=random.sample(range(100),random.randint(40,49))## randint()函数皆是闭区间，  注意复习random函数和逻辑字符的优先关系
list2=random.sample(range(100),random.randint(40,49))
print('list1: {}'.format(list1))
print('list2: {}'.format(list2))
print('The common integers (in the order of list2):')
for x in list2:
    if x in list1:
        print(x,end='')


