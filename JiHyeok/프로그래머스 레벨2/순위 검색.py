
def find(li_index,info,score):
    idx = 0
    while int(info[li_index[idx]][4]) < score :
        idx += 1
    return set(li_index[idx:])



def solution(info, queries):
    answer = []

    dic = dict()

    set_cpp = set()
    set_java = set()
    set_python = set()

    set_backend = set()
    set_frontend = set()

    set_junior = set()
    set_senior = set()

    set_chicken = set()
    set_pizza = set()

    set_language = set()
    set_work = set()
    set_exp = set()
    set_soul = set()

    set_all = set()
    list_score = []

    for i in range(len(info)):
        info[i] = info[i].split()
    
    for i in range(len(queries)):
        queries[i] = queries[i].replace('and','')
        queries[i] = queries[i].split()

    for i in range(len(info)):
        set_all.add(i)
        list_score.append(i)

        if 'cpp' in info[i]:
            set_cpp.add(i)
        if 'java' in info[i]:
            set_java.add(i)
        if 'python' in info[i]:
            set_python.add(i)
        
        if 'backend' in info[i]:
            set_backend.add(i)
        if 'frontend' in info[i]:
            set_frontend.add(i)

        if 'junior' in info[i]:
            set_junior.add(i)
        if 'senior' in info[i]:
            set_senior.add(i)
        
        if 'chicken' in info[i]:
            set_chicken.add(i)
        if 'pizza' in info[i]:
            set_pizza.add(i)

    dic['cpp'] = set_cpp
    dic['java'] = set_java
    dic['python'] = set_python

    dic['backend'] = set_backend
    dic['frontend'] = set_frontend

    dic['junior'] = set_junior
    dic['senior'] = set_senior

    dic['chicken'] = set_chicken
    dic['pizza'] = set_pizza

    dic['-'] = set_all

    list_score.sort(key=lambda x: int(info[x][4]))

    
    for query in queries:
        count = 0
        set_score = find(list_score,info,int(query[4]))
        li = list(dic[query[0]].intersection(dic[query[1]].intersection(dic[query[2]].intersection(dic[query[3]].intersection(set_score)))))
        
        answer.append(len(li))
    return answer
print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))

'''
    개발언어 : cpp,java,python
    직군 : backend, frontend
    경력 : junior, senior
    소울푸드 : chicken, pizza
    점수 : X값

    1.  첫번째로, 각 원소에 해당하는 집합들을 만들어준다.
        ex) cpp집합, java집합, python집합, backend집합 .... ~ pizza집합 까지

    2.  쿼리문을 순회 하는데, 각각의 쿼리문 마다 X(점수) 집합을 만들어준다.


    3.  각 쿼리문의 모든 조건을 교집합 시켜버리면 됨


'''