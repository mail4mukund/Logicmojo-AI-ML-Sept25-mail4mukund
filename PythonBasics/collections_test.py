dic={'1':'one','2':'two','3':'three'}
#print(dic['2'])
#print(dic['5'])
#print(dic.keys['5'])

for k in dic:
    print(k + '\t:\t'+dic.get(k)) 

print('get key value by other ways\n')

for k, v in dic.items():
    print(k + '\t:\t'+v) 
    

dic={'1':['one','I'],'2':['two','II'],'3':['three','III']}

for k, v in dic.items():
    print(k + '\t:\tEnglish:'+v[0]+'\tRoman:'+v[1]) 