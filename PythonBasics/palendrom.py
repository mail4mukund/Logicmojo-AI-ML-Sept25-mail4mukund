strInput=input('Enter a string: ')
strRev=strInput[::-1]   
if strInput==strRev:
    print('Given string is Palendrom')
else:
    print('Given string is not Palendrom')


passStatement=''
for i in range(5):
    if(i==0):
        pass
        print('pass :'+ str(i))
    else:
        print('else condition:'+str(i))