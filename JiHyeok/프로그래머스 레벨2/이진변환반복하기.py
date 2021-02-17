
def solution(s):
    answer = []
    count = 0
    zerocount = 0
    while s != '1': ### s 가 1이 될때 까지
        count += 1 ###변환한 횟수를 세어주는 count변수
        zerocount += s.count('0') ### 0의 개수를 세어주고
        s = s.replace('0','') ### 0을 모두 제거 한 다음
        s = bin(len(s))[2:] ### s를 2진수로 만들기

    answer = [count,zerocount]
        
    
    return answer

print(solution("110010101001"))