from collections import deque
def solution(numbers, target):
    count = 0
    queue = deque([])
    n = len(numbers)
    queue.append((numbers[0], 0))
    queue.append([-1*numbers[0],0])
    while queue:
        node, idx = queue.popleft()
        idx += 1
        if idx < n:
            queue.append((node+numbers[idx], idx))
            queue.append((node+-1*numbers[idx],idx))
        elif node == target:
            count += 1

    return count