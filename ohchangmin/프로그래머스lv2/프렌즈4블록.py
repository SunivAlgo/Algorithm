def solution(m, n, board):
    answer = 0
    char_board = [list(board[i]) for i in range(len(board))]  # board의 값은 문자열로 이루어져 문자열 안의 문자의 변경이 힘들기 때문에 모두 문자로 바꿔서 이차원리스트에 저장

    while True:
        check = [[False] * n for _ in range(m)]   # board 크기 만큼 False로 채워진 이차원 리스트 생성
        flag = False
        for i in range(m-1):  #4칸의 같은 부분이 존재 하면 char_board의 인덱스 위치를 check 인덱스 위치에 대입하여 true로 바꿔준다(true는 제거되는 부분을 의미)
            for j in range(n-1):
                if char_board[i][j] != '0' and char_board[i][j] == char_board[i][j+1] and char_board[i][j] == char_board[i+1][j] and char_board[i][j] == char_board[i+1][j+1]:
                    check[i][j] = check[i+1][j] = check[i][j+1] = check[i+1][j+1] = True
                    flag = True 
        if not flag:    # 제거할 부분이 없을 경우 종료
            break

        for i in reversed(range(m)):     # 맨 아래의 인덱스 부터 채워져야 하기 때문에 역순으로 반복문 돌림
            for j in range(n):
                if check[i][j]:     # 제거된 부분이라면 그 위에 있는 인덱스를 올라가며 순회하고 채워야할 문자를 찾는다.
                    for k in reversed(range(i)): 
                        if not check[k][j]:    #위에 제거 되지 않는 값이 있다면 그 값으로 바꿔주고 check 의 값도 바꿔줌
                            char_board[i][j] = char_board[k][j] 
                            check[i][j] = False  
                            check[k][j] = True  
                            break

        for i in range(m):  # 비워진 부분(True) 를 0으로 바꿔준다.
            for j in range(n):
                if check[i][j]:
                    char_board[i][j] = '0'

    for i in char_board: # 제거된 부분만큼 answer를 더함
        for j in i:
            if j == '0':
                answer += 1

    return answer


m = 6
n = 6
board = ["AABBEE","AAAEEE","VAAEEV","AABBEE","AACCEE","VVCCEE" ]
print(solution(m, n, board))
'''
m = 4
n = 4
board = ["ABCD", "BACE", "BCDD", "BCDD"]
print(solution(m, n, board))

m = 4
n = 5
board = ["AAAAA","AUUUA","AUUAA","AAAAA" ]
print(solution(m, n, board))

print(solution(2,2,["AA", "AA"]))
print(solution(2,2, ["AA", "AB"]))

print(solution(3,2, ["AA", "AA", "AB"]))
print(solution(4,2, ["CC", "AA", "AA", "CC"]))

print(solution(6,2, ["DD", "CC", "AA", "AA", "CC", "DD"]))
print(solution(8,2, ["FF", "AA", "CC", "AA", "AA", "CC", "DD", "FF"]))
print(solution(6,2, ["AA", "AA", "CC", "AA", "AA", "DD"]))
'''
'''
check = [[False] * n] * m 이런식으로 선언할경우 check[0][0] 을 바꿀경우 이차원 배열 안의 모든 첫번째 원소가 바뀜
'''