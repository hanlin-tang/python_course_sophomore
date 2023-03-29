a= float(input('Enter a score(0 <= score <=100): ' ))
if a >100:
    print('The score must be less than 100 or equal to 100')
elif a >=90:
    print('Grade: A')
elif a >=85:
    print('Grade: A-')
elif a >=82:
    print('Grade: B+')
elif a >=78:
    print('Grade: B')
elif a>=75:
    print('Grade: B-')
elif a>=71:
    print('Grade: C+')
elif a>=66:
    print('Grade: C')
elif a>=62:
    print('Grade: C-')
elif a>=60:
    print('Grade: D')
elif a>=0:
    print('F')
else :
    print ('The score must be greater than 0 or equal to 0')
