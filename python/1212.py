L=eval(input(''))
def func(L):
    "找到L内的所有质数并返回列表"
    list1=[]
    for i in range (2,L+1):
        k=2
        while k<i:
            if i%k==0:
                break
            else:
                k+=1
        else:
            list1.append(i)
    return list1

func(L)
print(list1)

