x=int(input('Enter a 4-digit number:'))
thousand=x//1000
hundred=x//100 %10
ten=x//10 % 10
unit=x % 10
print(thousand,hundred,ten,unit)
