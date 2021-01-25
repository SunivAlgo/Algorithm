def solution(skill, skill_trees):
    answer = 0
    m = {}
    n = 1
    for i in skill:
        m[i] = n
        n += 1
    
    for i in skill_trees:
        flag = True
        check = [0 for i in range(0, len(skill) + 1)]
        check[0] = 1
        for j in i:
            if j in m:
                if check[m[j]-1] == 1:
                    check[m[j]] = 1
                else:
                    flag = False
                    break
        if flag:
            answer += 1

    return answer

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

print(solution(skill, skill_trees))

"""
스킬 순서 별로 딕셔너리를 통해 설정을 해놓는다면 참조시 바로 참조가 가능할 것 같아서
딕셔너리로 먼저 스킬들을 저장했다. 그 후 체크 리스트를 skill_trees의 요소들을 참조할 때
마다 생성을 하고 skill_trees의 각각 요소의 문자들을 참조해 그 전의 스킬이 전에 나왔다는
것을 체크리스트로 파악하여 문제를 풀이 했다.
"""