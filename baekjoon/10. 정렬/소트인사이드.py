N = input()
list =[]
for i in N:
    list.append(i)

list.sort(reverse=True)
for i in list:
    print(i,end='')
