arr = [4,4,4,3,3]
answer = []
indx = 0
siz = len(arr) - 1
while indx != siz:
    if arr[indx] == arr[indx+1]:
        
        del arr[indx]
        siz -= 1
    else:
        indx += 1
answer = arr
print(arr)



