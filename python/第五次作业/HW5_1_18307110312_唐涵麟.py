import random
alist= random.sample(range(-50,50),20)
blist=alist[:10]
clist=alist[10:]
blist.sort()
clist.sort(reverse=True)
blist.extend(clist)
print('The original list is: \n {}'.format(alist))
print('The first half is sorted in ascending order, the second half in desending order:')
print(blist)
