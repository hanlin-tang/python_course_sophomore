"""
基于Markov过程的文本生成:
markov_dict:  { 'word': [next_words.....], ..... }
"""

import os
import random

markov_dicts = {'':[]}   # Start of Sentence
sentence_sep = '.?!'    # 句子结束标志

def parse(text):
    """ 分析text，产生相应的dict"""
    import re
    
    pat1firstwords=re.compile(r'(! |\. |\? )(\b[a-zA-Z\']+\b)')
    list1=pat1firstwords.findall(text)
    list1=[i[1] for i in list1]
    
    
    
    
    pattallwords=re.compile('([a-zA-Z\']+\\b\?*\.*!*)')     #'与 ([a-zA-Z]+\\b\?*\\b)'的不同,以及为了输出后面跟着的标点符号
    allwords=pattallwords.findall(text)
    #print(allwords)
    
##    keys=[]
##    for i in range(len(allwords)):
##        key=allwords[i]
##        keys.append(key)
##        
##        if i+1<len(allwords):
##            value=allwords[i+1]                           
##        markov_dicts.setdefault(key,[]).append(value)  #原地更新字典  #会出现连续重复时露匹配的现象
##        
##        
##    
##    markov_dicts['']=list1
    
    return allwords   
        
    
    


    
    pass

##def generate(num_sentences=1, word_limit=20):
##    """ 根据前面调用parse得到的dict，随机生成多个句子"""
##    r=[]
##    j=0
##    while j<num_sentences:
##        
##    
##        senlist=[]
##        fir=markov_dicts['']
##        a=random.choice(fir)
##        senlist.append(a)
##        i=1
##        while i<word_limit:
##            if a.endswith('.') or a.endswith('!') or a.endswith('?') :
##                
##                break
##            
##            seq=markov_dicts[a]
##            next_=random.choice(seq)
##            senlist.append(next_)
##            a=next_
##        
##            
##            i+=1
##        sen=' '.join(senlist)
##        r.append(sen)
##        
##
##        j+=1
##    return r
    

def markov_main():

    with open('test.txt') as f:
        list1=f.readlines()
        list2=[i.strip() for i in list1]
    
        test=' '.join(list2)
        
        
        newlist=[i.lower() for i in parse(test)]
        print(newlist)
    with open('dictionary.txt') as g:
        list3=g.readlines()
        list4=[i.strip() for i in list3]
    
        source=' '.join(list4)
        newlist2=[i.lower() for i in parse(source)]
        result=[]
        print(newlist2)
    for i in newlist:
        if i in newlist2:
            i=i+'\t'
            result.append(i)
    print(result)
    with open('repeat items.txt','w') as r:
        r.writelines(result)
            
    

        

        
if __name__ == '__main__':
    markov_main()
  
input('press<enter>')   

