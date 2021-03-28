x, y, w, h = map(int, input().split())
d_list = [x, y, w-x, h-y]
print(min(d_list))