def solution(answers):
    n = len(answers)
    pA = [1, 2, 3, 4, 5]
    pB = [2, 1, 2, 3, 2, 4, 2, 5]
    pC = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    pattern = [pA, pB, pC]
    idx = [0,0,0]
    ans = {1:0,2:0,3:0}
    for i in range(n):
        for j in range(3):
            if pattern[j][idx[j]] == answers[i]:
                ans[j+1] += 1
                
            idx[j] += 1
            if idx[j] >= len(pattern[j]):
                idx[j] = 0
      
    print(ans)
    answer = []
    max_point = max(ans.values())
    for k,v in ans.items():
        if v == max_point:
            answer.append(k)
    return answer