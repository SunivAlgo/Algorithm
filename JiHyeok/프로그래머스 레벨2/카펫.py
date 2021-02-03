
def solution(brown, yellow):
    answer = []
    garo = 0
    sero = 0
    for i in range (1,yellow + 1):
        if yellow % i == 0:
            if ((yellow / i) + i) * 2 + 4 == brown:
                sero = i + 2
                garo = yellow/i + 2
                answer.extend([int(garo),sero])
                break   
    return answer
print(solution(10,2))


'''
    1.  안의 노란색 타일을 바깥의 갈색타일이 감싸는 구조로 생각
    2.  1번에 따라서, 갈색의 타일 개수 = (노랑 세로 + 노랑 가로) * 2 + 4 를 도출
    3.  brown과 yellow가 주어지면, yellow를 구성할수 있는 곱셈세트를 훑으면서 brown의 개수와 같은지 비교하면 된다.
'''