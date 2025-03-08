def solution(number, k):
    answer = ''
    max = 0
    n = len(number)
    
    stk = []
    for num in number:
        # 값들어있고, 뺄게남아있고, 탐색대상보다 작으면 계속 pop, 제거수--
        while stk and k>0 and stk[-1]<num: 
            stk.pop()
            k -= 1
        
        # 아니면 추가
        stk.append(num)
            
        # 줄인 코드 위로
        # if not stk: # 비어 있으면 삽입
        #     stk.append(num)
        #     continue
        # if k > 0: # 들어있을땐 탐색 대상과 비교
        #     while stk[-1] < num:
        #         stk.pop()
        #         k -= 1
        #         if not stk or k < 1:
        #             break
        # stk.append(num) # 남은 뒤에 값들을 삽입            
    # return ''.join(stk)
    return ''.join(stk) if k == 0 else ''.join(stk[:-k]) # ('98576',2) 같은 케이스