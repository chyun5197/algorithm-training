from collections import deque
def solution(people, limit):
    answer = 0    
    people = deque(sorted(people))
    while people:
        if len(people)==1:
            del people[-1]
        elif people[0]+people[-1] <= limit:
            del people[0]
            del people[-1]
        else:
            del people[-1]
        answer+=1
    return answer