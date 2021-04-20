from collections import Counter

print(Counter())
print(Counter(['a', 'b', 'b', 'c', 'c', 'c'])) # list
print(Counter('abbccc')) # string
# print(Counter({'red': 4, 'blue': 2})) # 잘안씀, dict
# print(Counter(cats=4, dogs=8)) # 잘안씀, keyword args

# 기본 사용 방법은 dict와 비슷하다.
print("\n===== basic =====")
my_list = ["Apple", "Banana", "Coconut"]
c = Counter(my_list)
print(c["Apple"])
print(c["Durian"])

# most_common(n)은 가장 빈번한 순서대로 n개를 반환한다.
# 알고리즘 문제 풀이에 메소드 중 most_common이 가장 많이 쓰임.
print("\n===== most_common method =====")
c = Counter('abracadabra')
print(c)
print(c.most_common(3))
print(type(c.most_common(3)), type(c.most_common(3)[0])) # list of tuple로 반환

# elements()는 Counter를 개수에 맞는 iterator로 반환한다.
print("\n===== elements method =====")
c = Counter(a=4, b=2, c=0, d=-2)
print(c)
print(c.elements()) # iterator로 반환
print(list(c.elements())) # 0 이하(c, d)는 무시

# update(new_lisst)는 추가할 때 사용한다.
print("\n===== update method =====")
my_list = ["Apple", "Banana", "Coconut"]
new_list = ["Apple", "Durian"]
c = Counter(my_list)
print(c)
c.update(new_list)
print(c)

# cards[x] vs cards.get(x)
cards = Counter([1, 2, 2, 3, 3, 3])
for i in range(5):
    print(cards[i], cards.get(i))