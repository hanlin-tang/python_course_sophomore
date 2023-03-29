m=[[2,3,4],[4,5,6]]
for rows in m:
    for elem in rows:
        print(elem,end=',')
    print()         #每一行结束用于换行

# 对所有的矩阵元素求和
total=0
for rows in m:
    for elem in rows:
        total+=elem
print(total)
totals=0
for rows in m:
    totals=totals+sum(rows)
print(totals)
