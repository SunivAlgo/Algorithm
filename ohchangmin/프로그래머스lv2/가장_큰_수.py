import itertools

def solution(num): 
    num = list(map(str, num)) 
    num.sort(key = lambda x : x*3, reverse = True)
    return str(int(''.join(num)))

'''def solution(numbers):
    answer = '0'
    arr = list(itertools.permutations(numbers))
    for i in arr:
        s = ""
        for j in i:
            s += str(j)
        if int(answer) < int(s):
            answer = s
    return answer'''

'''def solution(numbers):
    answer = ''
    a = []
    for i in numbers:
        a.append(str(i))

    max_length = len(max(a, key=len))
    for i in range(0, len(a)):
        c = a[i][-1]
        a[i] = a[i].ljust(max_length, c)

    ind = []
    for i in range(0, len(a)):
        ind.append(i)
    a = list(zip(a, ind))
    a.sort(key=lambda x : x[0], reverse = True)

    for i in a:
        answer += str(numbers[i[1]])

    return answer
'''

numbers = [40, 403]
print(solution(numbers))