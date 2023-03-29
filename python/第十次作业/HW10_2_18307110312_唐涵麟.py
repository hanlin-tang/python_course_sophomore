a=input('Enter 2 words(separated with comma):')
word1,word2=a.split(',')
a,b=a.split(',')
word1=word1.lower()
word2=word2.lower()
word1=set(list(word1))
word2=set(list(word2))
st=sorted(word1)
ed=sorted(word2)
if st==ed:
    print('"{}" and "{}" are analogous'.format(a,b))
else:
    print('"{}" and "{}" are not analogous'.format(a,b))
        
