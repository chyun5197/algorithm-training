def check(a,b):
    cnt = 0
    
    for i in range(len(a)):
        if a[i] != b[i]:
            cnt += 1
    return cnt


def solution(begin, target, words):
    answer = 0
    visited = [False] * len(words)
    if target not in words:
        return answer
    
    result = []
    def dfs(v, step):
        if v == target:
            result.append(step) 
            return

        for i in range(len(words)):
            if check(v, words[i]) == 1 and not visited[i]:
                visited[i] = True
                dfs(words[i], step+1)
                visited[i] = False
    
    dfs(begin, 0)
    return min(result)