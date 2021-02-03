def solution(arr):
    answer = []
    for i in range(0,len(arr)-1):
        if(arr[i] != arr[i+1]):
            answer.append(arr[i])
    answer.append(arr[len(arr)-1])

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    return answer