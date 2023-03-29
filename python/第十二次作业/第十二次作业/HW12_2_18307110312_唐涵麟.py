import re
text  = input('Enter some text:')
a=text.split(' ')
wordsnummber=len(a)
maxnumber=0
for i in a:
    list1=re.findall('\w',i)
    lenth=len(list1)
    if lenth>maxnumber:
        maxnumber=lenth
        maxlist=list1
    word=''.join(maxlist)
        

print('There are {} words in total'.format(wordsnummber))
print('The longest word is {}'.format(word))

