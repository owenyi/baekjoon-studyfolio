def find_parent(parent, x):
    if parent[x] == x: return x
    parent[x] = find_parent(parent, parent[x]) # memoization
    return parent[x]

# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a < b: parent[b] = a
#     else: parent[a] = b

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a == b: return
    parent[b] = a # a <- b

def weighted_union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a == b: return
    parent[a] += parent[b]
    parent[b] = a