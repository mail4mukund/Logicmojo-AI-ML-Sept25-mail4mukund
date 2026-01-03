a, b=map(int, input('Enter two - Must be numeric only').split())
print(a)
print(b)

var='Mukund kumar'
st=set(var)
print(var)
print(st)

dic=dict({"name":"Mukund Kumar", "age":45, "course":[1,2,3,4,5]})
for d in dic:
    print(f"Key '{d}' and value is '{dic[d]}'")

del(dic)

def SayYesNo(keyName):
    if(keyName=='mukund'):
        return 'Yes'
    elif(keyName=='kumar'):
        return 'Maybe'
    else:
        return 'No'
    
print(SayYesNo('mukunds'))

#print(map(SayYesNo, ['mukund', 'kumar', 'chautham', 'hello']))