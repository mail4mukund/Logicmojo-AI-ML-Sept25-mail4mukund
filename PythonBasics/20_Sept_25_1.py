# a=(1,2,'a')
# print(hash(a))

# #a=[1,2,3]
# #print(hash(a)) #mutable so not hashed

# setTest={a,1,'k'} # Sets are nohomogenous  in nature
# print(setTest)
# setTest=setTest.add('m')
# print(setTest)

# #tuple inside tuple also we can use
# tup=(a,1,2)
# print(tup)
# print(tup[0][2])

# #Extend and Append
# l=[1,2,3]
# l.append(4)
# l.extend(['k'])
# print(l)

#Dictionary
'''
Unordered
indexed by key to get vlaue like d['ky']
'''

dic=dict(name='mukund kumar',age=25, clas='pythem')


dic1=dict({'name':'mukund kumar','age':25, 'clas':'pythem'})


dic.update(dic1)

for i in dic.items():
  print(i)

#update vs merge in dictionary
#Use case of JSON vs Dictionary
#Node= link list
#Head = 1st Node
#Tail = last Node
#singly link list 
#doubly link list

