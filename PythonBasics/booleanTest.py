print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

x = isinstance("Hello", (float, int, str, list, dict, tuple))

print('x = isinstance("Hello", (float, int, str, list, dict, tuple))')
print(x)


class myObj:
  name = "John"

y = myObj()

x = isinstance(y, myObj)

print('x = isinstance(y, myObj)')
print(x)

thislist = ["apple", "banana", "cherry"]
print(thislist)