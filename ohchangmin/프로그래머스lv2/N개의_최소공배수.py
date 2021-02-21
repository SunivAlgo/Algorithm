def solution(arr):
    new_arr = []
    arr.sort()

    for i in range(0, len(arr)):
        flag = True
        for j in range(i+1, len(arr)):
            if arr[j] % arr[i] == 0:
                flag = False
                break
        if flag:
            new_arr.append(arr[i])

    num = max(new_arr)
    while True:
        flag = True
        for i in new_arr:
            if num % i != 0:
                flag = False
                break
        if flag:
            return num
        num += 1

arr = [2,6,8,14]
print(solution(arr))

'''
arr 안에 공배수 관계가 있는 숫자는 제거 하고 새로운 배열을 만든다.
[2,6,8,14] 여기서 2의 공배수가 다른 수에서 보여지니 2를 제거한다.
[6,8,14] 이 수 중에서 가장 큰 수 부터 시작하여 +1을 계속 해주면서 
모든 수에 나누어 지는지 확인한다.

다른 풀이를 보니 내가 푼 방법은 좋지 않는것 같다.
x*y/ x,y의 최대 공약수 = 최대공배수
from fractions import gcd   gcd(x,y) = 최대 공약수 알아두기
'''