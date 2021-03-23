def solution(N, number):
    if N == number:     # 밑에서 수행되는 주요 코드는 retrun 되는 수를 2부터 검사하기 때문에 따로 처리한다
        return 1
    
    d = {}
    n = N
    for i in range(1, 9):   #{1: {5}, 2: {55}, 3: {555}, 4: {5555}, 5: {55555}, 6: {555555}, 7: {5555555}, 8: {55555555}} 이런식으로 초기화
        d[i] = set([n])
        n *= 10
        n += N

    for i in range(1, 8):   
        for j in range(1, i+1):
            if i+j > 8:     #최솟값은 8보다 작아야 하기 때문에 검사하지 않음
                break
            for k in d[i]:     #d 딕셔너리를 계속 점점 업데이트함
                for l in d[j]:
                    d[i + j].add(k + l)
                    d[i + j].add(abs(k - l))    # 1-5 같은경우 -4이지만 어차피 5-1같은 경우도 구해야 하기 때문에 절댓값을 넣어줌
                    d[i + j].add(k * l)     
                    if k != 0 and l != 0:   #오류방지
                        d[i + j].add(k // l)
            if number in d[i + j]:  #만든 set에 number가 있다면 return 하고 끝
                return i+j

    return -1


print(solution(5, 5))
print(solution(5, 12))
print(solution(5, 31168))
print(solution(5, 22))
print(solution(5, 4))
