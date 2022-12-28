while True:
    numbers = list(map(int, input().split()))
    maxi = max(numbers)
    if sum(numbers) == 0:
        break
    numbers.remove(maxi)
    if numbers[0]**2 + numbers[1]**2 == maxi**2:
        print("right")
    else:print("wrong")