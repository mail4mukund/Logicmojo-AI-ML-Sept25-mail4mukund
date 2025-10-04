"""
Q3 : Description You will be given a string with a lot of brackets. You have to print if the brackets are balanced or not. Remember, there are three types of brackets: ‘( )’, ‘{ }’ and ‘[ ]’.

s = '{{{[[[[]]]}(())'
s2 = '{{{{[[[[((()))]]]]}}}}'
Input: A string

Output: Yes, if the brackets are balanced. No otherwise.
"""
#s = '{{{[[[[]]]}(())'
s = '{{{{[[[[((()))]]]]}}}}'
maxMatchIndex=int(len(s)/2);
lastIndex=len(s)-1
for a in s:
    if((a=='{' and s[lastIndex]=='}') or (a=='['and s[lastIndex]==']') or (a=='('and s[lastIndex]==')')):
        lastIndex-=1
        continue
    elif(lastIndex<maxMatchIndex-1):
        print('Unbalanced brackets')
        break
