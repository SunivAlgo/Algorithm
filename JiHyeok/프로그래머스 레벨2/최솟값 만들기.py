
def solution(A,B):
    answer = 0

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    ### 리스트 정렬 
    ### A는 오름차순, B는 내림차순
    A.sort()
    B.sort(reverse = True)


    ### A와 B에서 원소하나씩 뽑아서 곱셈
    for a,b in zip(A,B):
        answer += a * b

    return answer

print(solution([1, 4, 2] , [5 , 4 , 4]))