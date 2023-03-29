x = int (input('输入一个三位数：'))
hundred = x//100
ten = (x-100*hundred)//10
unit =  (x-100*hundred-ten*10)/1
print (hundred,ten,unit)
input('Press <Enter>')
