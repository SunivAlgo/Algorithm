import itertools

def solution(numbers):
    answer = 0
    i_num = []
    for i in numbers:
        i_num.append(int(i))

    m = {}
    for i in range(1, len(numbers)+1):
        p = list(itertools.permutations(i_num, i))
        for j in p:
            s = ""
            for k in j:
                s += str(k)

            num = int(s)
            if not(num in m):
                m[num] = 1
                flag = True        
                if num >= 4:
                    for k in range(2, int(num ** 0.5 + 1)):
                        if num % k == 0:
                            flag = False
                elif num == 1 or num == 0:
                    flag = False
                
                if flag:
                    answer += 1

    return answer

numbers = "011"
print(solution(numbers))