def solution(sizes):
    maxA, maxB = 0, 0    
    for datas in sizes:
        datas.sort(reverse=True)
        if datas[0] > maxA:
            maxA = datas[0]
        if datas[1] > maxB:
            maxB = datas[1]
    
    # print(*sizes, sep='\n')

    return maxA*maxB