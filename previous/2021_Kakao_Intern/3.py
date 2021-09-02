def up(dll, k, x):
    for _ in range(x):
        pre, _ = dll[k]
        k = pre
    return k


def down(dll, k, x):
    for _ in range(x):
        _, post = dll[k]
        k = post
    return k


def delete(dll, trash_can, k):
    pre, post = dll.pop(k)
    trash_can.append((k, pre, post))

    if post is None:  # 삭제될 노드가 마지막 노드라면
        dll[pre][1] = None
        return pre
    else:
        if pre is None:  # 삭제될 노드가 처음 노드라면
            dll[post][0] = None
        else:
            dll[pre][1] = post
            dll[post][0] = pre
        return post


def recover(dll, trash_can):
    l, pre, post = trash_can.pop()
    dll[l] = [pre, post]
    if pre is not None:
        dll[pre][1] = l
    if post is not None:
        dll[post][0] = l


def solution(n, k, cmd):
    # double linked list
    dll = {0: [None, 1], n - 1: [n - 2, None]}
    for i in range(1, n - 1):
        dll[i] = [i - 1, i + 1]

    # stack
    trash_can = []

    for c in cmd:
        if c[0] == 'U':
            x = int(c[2:])
            k = up(dll, k, x)
        elif c[0] == 'D':
            x = int(c[2:])
            k = down(dll, k, x)
        elif c[0] == 'C':
            k = delete(dll, trash_can, k)
        elif c[0] == 'Z':
            recover(dll, trash_can)

    return ''.join(['O' if dll.get(i) else 'X' for i in range(n)])


n, k = 8, 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
print(solution(n, k, cmd))