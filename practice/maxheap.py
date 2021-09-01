import heapq

array = [4, 14, 7, 2, 8, 1]
array = [(-x, x) for x in array]
print(array)

heapq.heapify(array)
print(array)

array = [16, 5, 11, 3]
array = [(-x, x) for x in array]
heapq.heappush(array, (-18, 18))
print(array)

print(heapq.heappop(array)[1])
print(array)