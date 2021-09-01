import heapq

array = [4, 14, 7, 2, 8, 1]
heapq.heapify(array)
print(array)

heapq.heappush(array, 0)
print(array)

print(heapq.heappop(array))
print(array)