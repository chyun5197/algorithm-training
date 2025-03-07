# 순열
from itertools import permutations

def isPrime(n): # 소수면 True
    if n < 2:
        return False

    for i in range(2, n):
        if n%i==0:
            return False
    return True

def solution(numbers):
    answer = 0
    numSet = set()
    for c in range(1, len(numbers)+1):
        for nums in permutations(numbers, c):
            # print(nums)
            num = ''
            for n in nums:
                num += n
            numSet.add(int(num))
    print(numSet)
    for e in numSet:
        if isPrime(e): answer+=1
    return answer