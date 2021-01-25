def solution(n):
    if n == 1:
        return [1]

    arr = []
    for i in range(1, n+1):
        a = [0 for j in range(0, i)]
        arr.append(a)

    x = 0; y = 0
    bottom = n-1; right = n-1; top = 1
    num = 1
    command = "down"

    while arr[y][x] == 0:
        arr[y][x] = num
        num += 1
        if command == "down":
            y+=1
            if y == bottom:
                command = "next"
                bottom -= 1
        elif command == "next":
            x += 1
            if x == right:
                command = "up"
                right -= 2
        elif command == "up":
            y -= 1
            x -= 1
            if y == top:
                command = "down"
                top += 2
                
    return sum(arr, [])

print(solution(6))

'''
먼저 n의 갯수만큼 계단식 모양의 리스트를 0으로 초기화 시켜 만든다.
0,0 인덱스부터 시작하여 인덱스 값이 0이면 1씩 증가 시킨 값을 넣어주고 0이 아니면 break 한다.
그리고 command 변수를 두어서 인덱스가 어디로 이동할 것인지 값을 넣는다. 
아래 오른쪽 위쪽에 경계값을 넣어주어 그 경계 값에 도달 시 command 변수를 다른 방향으로 바꾼다.
여기서 밑에 경계선은 1씩 감소하지만 오른쪽과 위쪽 경계선은 인덱스가 이동하면서 값이 채워지기 때문에
2씩 증가하는 것이 핵심이다.
위와 같은 방식은 다음 인덱스가 0인지의 여부에 따라 반복문이 진행 되기때문에 n이 1이라면 다음 인덱스를
참조시 에러가 나서 그냥 [1]을 처음부터 반환한다.
'''