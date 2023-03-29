t=[a*100+b*10+c for a in range(1,4) for b in range(1,10) for c in range(1,10)]
for one in t:
    two = one * 2
    three = one * 3
    string=str(one)+str(two)+str(three)
    group=set(tuple(string))
    if (len(group)==9 and three<1000 and '0' not in str(two) and '0' not in str(three) ):
        print(one, two, three)
