# 풀이 참고한 문제 : https://velog.io/@eehwan/프로그래머스-풍선-터트리기-파이썬 , https://kobumddaring.tistory.com/28
def solution(a):
    ans = [0 for _ in range(len(a))]
    l_M = r_M = float("inf")

    for i in range(len(a)):
        if a[i] < l_M:
            l_M = a[i]
            ans[i] = 1
        if a[-1-i] < r_M:
            r_M = a[-1-i]
            ans[-1-i] = 1
    return sum(ans)

    
print(solution([9,-1,-5]))
print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))
print(solution([1,2,3,4,5]))


#서울대,연대,아산,서울 삼성병원, 성모병원, 고려대 병원 --> 의학공학교실, 의료정보학교실

"""
가장 작은 수를 가진 풍선은 남을 수 있다. 큰 풍선을 다 터뜨리면 결국 제일 작은 수 풍선 하나만 남는다.
작은 수 또한 터트리기 가능, 번호가 더 작은 풍선을 터트릴 수 있는 기회 1회가 있음

"""