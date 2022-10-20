n = int(input())
inp = n
five = n // 5

ea = 0
brk = False

for i in range(five*5, -1, -5):
    n = inp
    if brk == True:
        break
    ea = 0
    n = n - i
    ea += i // 5

    three = n // 3

    if n == 0:

        break
    for j in range(three*3, -1, -3):

        n = n - j
        ea += j // 3

        if n == 0:

            brk = True
            break
    if i == 0 and brk == False:
        ea = 0
        break
                
if ea == 0:
    print("-1")
else:
    print(ea)
