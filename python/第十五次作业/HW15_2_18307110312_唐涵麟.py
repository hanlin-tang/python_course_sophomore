def extract_data_list(text):
    alist=text.split('\n')
    data_list=[i.strip().split(',') for i in alist if not i.startswith('#') and i!='' ]
    for i in data_list:
        i[2:3]=''
    data_list=[tuple(i) for i in data_list]
    
    return data_list


def construct_movies_by_director(data_list):
    
    dic={}
    for i in data_list:
        key=i[3]
        value=i[:3]
        dic.setdefault(key,[])
        if value in dic[key]:
            
            raise Exception('重复数据:{}'.format(value[1]))
         
            dic.setdefault(key,[]).append(value)   

    
        
    print(dic)
    

if __name__=='__main__':
    text2 = '''#年份,电影名,产地,票房,导演
   2013,Rush,US/UK,26.9,Ron Howard
2001,A Beautiful Mind,US,171,Ron Howard   
   2013,Rush,US/UK,26.9,Ron Howard   

2008,Hunger,UK,154,Steve McQueen   
'''
    text1= '''#年份,电影名,产地,票房,导演
   2013,Rush,US/UK,26.9,Ron Howard   
2001,A Beautiful Mind,US,171,Ron Howard   

  2008,Hunger,UK,154,Steve McQueen  
'''
    data_list=extract_data_list(text1)
    
    construct_movies_by_director(data_list)
    data_list=extract_data_list(text2)
    
    construct_movies_by_director(data_list)

