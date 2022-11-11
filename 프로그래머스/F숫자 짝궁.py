"""131128"""
from collections import OrderedDict

answer =''
x, y = "5525", "1255"

for i in range(len(x)):
    if y.find(x[i]) != -1:
        print(i)
        answer += x[i]
answer = ''.join(OrderedDict.fromkeys(answer))

answer = ''.join(sorted(answer,reverse=True))
if answer == '':
    answer = "-1"
print(answer)