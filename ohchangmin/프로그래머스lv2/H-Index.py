def solution(citations):
    citations.sort()
    for i in range(len(citations), 0, -1):
        if citations[len(citations) - i] >= i and len(citations) - i <= i:
            return i
    return 0

citations =	[0]	
print(solution(citations))

'''
먼저 citations를 정렬 시키고 최대값을 만나면 바로 break가 될수 있게
역순으로 참조한다. 조건문은 비교값 i보다 더 많은 값들이 i이상으로 
존재하고 그 외의 값들이 i 이하로 존재하면 i를 반환한다. 조건문에 만족 안할시
0을 반환한다.
'''