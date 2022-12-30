from heapq import heappush, heappop

nums = [4, 1, 7, 3, 8, 5]
heap = []

for i in nums:
    heappush(heap, (-i, i)) # (우선순위, 값) 

    # 음수가 된 우선순위를 인덱스로 이용 하면 수가 클수록 더 작아지니까 우선순위가 반대로 되고 [1]로 인덱스에 접근?

print(heap) # => [(-8, 8), (-7, 7), (-5, 5), (-1, 1), (-3, 3), (-4, 4)]
while heap:
    print(heappop(heap)[1], end=' ')