import itertools
import math
def powerset(nlist):
    subset = set()
    for i in range(1, len(nlist) + 1):
        temp = list(map(''.join, itertools.permutations(nlist, i)))
        subset.update(temp)
    return set(map(int, subset))

def solution(numbers):
    answer = 0
    nlist = list(numbers) # 리스트화
    subset = powerset(nlist) # 진부분 집합
    for i in subset:
        if i == 2 or i == 3: 
            answer += 1
            continue
        temp = math.floor(math.sqrt(i))
        for j in range(2, temp + 1):
            if i % j == 0:
                break
            if j == temp:
                answer += 1
    return answer
print(powerset("9999999"))
print(solution("1276543"))