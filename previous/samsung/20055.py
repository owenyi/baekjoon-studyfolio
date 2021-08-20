from collections import deque

N, K = map(int, input().split())
belt = deque(map(int, input().split()))
robot = deque([0 for _ in range(N)])

stage = 0
cnt = 0
while cnt < K:
    belt.rotate()
    robot.rotate()
    #if robot[-1] == 1: robot[-1] = 0 # 이렇게 할 필요 없고
    robot[-1] = 0 # 그냥 이렇게 하면 됨
    for i in range(N - 2, -1, -1):
        if robot[i] == 1 and robot[i + 1] == 0 and belt[i + 1] > 0:
                robot[i], robot[i + 1] = 0, 1
                belt[i + 1] -= 1
                if belt[i + 1] == 0: cnt += 1
    robot[-1] = 0 # 여기서도 해야됨
    if robot[0] == 0 and belt[0] > 0:
        robot[0] = 1
        belt[0] -= 1
        if belt[0] == 0: cnt += 1
    stage += 1

print(stage)