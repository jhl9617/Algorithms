from heapq import heappush, heappop, heapify

heapp = []

#heap push
heappush(heapp, 4)
heappush(heapp, 1)
heappush(heapp, 7)
heappush(heapp, 3)

print(heapp)

#heap pop heapp[0]째 원소 꺼내기
heappop(heapp)
print(heapp)

#heapp 루트원소 읽기

print(heapp[0])

#heapp[1]에 항상 두번째로 큰 원소가 있다는 보장이 없음
#heappop을 실행할때마다 이진트리를 재배치 하기때문에
#heappop을 실행하고나서 heapp[0]을 실행 해야 두번째로 큰 값 찾을 수 있음
print(heapp[1])


#기존 리스트를 힙으로 바꾸려면 heapify
heap2 = [4, 1, 7, 3, 8, 5]
heapify(heap2)
print(heap2)
