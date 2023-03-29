import random
a = random.sample(range(1,1000), 10)
print ('10 random integers: ',a)
print ('The max is: %s '% max(a))
print ('The min is: %s '% min(a))
print ('The average is: %s '% (sum(a)/len(a)))
