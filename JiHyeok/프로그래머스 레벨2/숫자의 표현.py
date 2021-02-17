def solution(n):
    answer = 0
    for i in range(1,n+1):

        if i % 2 == 1: ### i == 홀수

            if n % i == 0: ### 1번

                if n // i < i // 2: ### 3번
                    break

                answer += 1
        else:   ### i == 짝수

            if n % i == i // 2: ### 2번

                if n // i <= i // 2: ### 3번
                    break

                answer += 1

    return answer

print(solution(15))

'''
    1.  n을 1 ~ n 까지의 홀수(i) 로 나누었을 때 나머지 = 0 이면 answer++

    2.  n을 1 ~ n까지의 짝수(i) 로 나누었을 때 나머지가 i / 2 이면 answer ++

    3.  1번, 2번을 판단하기 전에,
        n을 i로 나누었을 때의 몫이 i // 2보다 작은지 체크해야 한다.

        ex))))))))

        n = 36 , i = 8, n//i = 4

        만약 36이 i(8)개의 연속된 자연수로 이루어졌다고 가정할 시
        
        x x x 4 x x x x         같은 구조를 띄게 된다

        4 앞에는 1,2,3 이 들어갈 수 있으므로 이제 1번 or 2번을 체크해 주면 된다.


        ex)))))))))

        n = 36, i = 10, n//i = 3

        만약 36이 i(10)개의 연속된 자연수로 이루어 졌다고 가정할 시

        x x x x 3 x x x x x     같은 구조를 띄게 되는데

        3앞에는 4개나 들어갈 자연수가 없으므로 i = 10일 때 break를 걸어주면 된다.

'''