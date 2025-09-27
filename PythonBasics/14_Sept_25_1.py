try:
    l=[0,3,4,5,6,8,9,19]
    print(l[:-1:2])

    a=12
    #a/0
    print(type(a))
    a="mukund"
    print(type(a))
    a/12
    x=20
    if(x>10):
    #print('More than 10')
        pass
    elif x>19:
        print('True 19')
    else:
        print('else')
except ZeroDivisionError as e:
    print('ZeroDivisionError we are gettging: '+ str(e))
except ValueError as e:
    print('ValueError we are gettging'+ str(e))
except Exception as e:
    print('Some error we are gettging' + str(e))