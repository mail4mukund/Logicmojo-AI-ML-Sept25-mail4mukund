inp=input('Enter a string: ')
result=''.join(sorted(set(inp), key=inp.index))
print(result)