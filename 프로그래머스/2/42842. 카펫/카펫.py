def solution(brown, yellow):
    # 가로,세로 개수
    # b = [w+2, h+2]
    # y = [w, yellow//w] # 가로>=세로 w^2 >= yellow
    # yellow = w*h
    # brown = (w+2)*2 + (yellow//w+2)*2 - 4
    answer = []
    for width in range(yellow, 0, - 1):
        if width**2 < yellow:
            break
        if  yellow/width != yellow//width:
            continue
        if (width+2)*2 + (yellow//width+2)*2-4 == brown:
            answer += [width+2, yellow//width+2]
            print(width)
            break
    
    return answer # 브라운 가로 세로