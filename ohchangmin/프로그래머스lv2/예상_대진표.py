def solution(n,a,b):
    answer = 0

    arr = [i for i in range(1, n+1)]
    while True:
        answer+=1
        r = pow(2, answer)
        for i in range(0, n, r):
            arrr = arr[i:i+r]
            print(arrr)
            if a in arrr and b in arrr:
                return answer

print(solution(8,4,7))

'''
[1, 2]
[3, 4]
[5, 6]
[7, 8]
[1, 2, 3, 4]
[5, 6, 7, 8]
[1, 2, 3, 4, 5, 6, 7, 8]
이런식으로 배열들을 구하여 a, b가 배열안에 있는지 확인한다.
값이 배열안에 존재하는지 확인해야하고 배열도 계속 만들어 줘야해서
느린 속도를 보여준다.

새로운 방법:
a와 b를 최종적으로
둘다 1이 될때까지 2로 나눠서 (홀수 일때는 나누고 1을 더함) 
나눌떄 마다 answer에 1을 더하는 방식이 훨씬 빠르다.
'''
