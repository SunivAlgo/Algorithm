
def solution(s):

    ### 문자열 나누기
    s = s.split() 

    ### s 안의 리스트들의 원소들을 int자료형으로 바꾸기
    s = list(map(int,s))

    ###최소 최대값 찾기
    min_n = min(s) 
    max_n = max(s)
    
    answer = str(min_n) + ' ' + str(max_n)

    return answer

print(solution("-1 2 3 4"))
