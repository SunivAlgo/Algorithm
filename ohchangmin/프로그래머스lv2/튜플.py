def solution(s):
    answer = []
    d = {}
    num = ""
    for i in s:
        if i >= '0' and i <= '9':
            num += i
        else:
            if len(num) != 0:
                if num in d:
                    d[num] += 1
                else:
                    d[num] = 1
            num = ""

    answer = sorted(d, key= lambda x:d[x], reverse=True)
    return list(map(int, answer))

s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
print(solution(s))

'''
배열안에 있는 숫자들을 딕셔너리키값으로 넣고 중복되는 수만큼 키에 대한
value를 더해준다.
해당 딕셔너리를 value를 기준으로 내림차순 정렬한다.
'''