"""436885"""

s = "3people unFollowed me"	
answer = ''
upperr = True
answ = ''
for i in s:
    if upperr == True:
        answ += i.upper()
        upperr = False
    elif i == ' ':
        upperr = True
        answ += ' '
    else:
        answ += i.lower()
    
        
answer = answ
print(answer)