def solution(s):
    li = s[1:-2].split('}')
    answer = []
    set_tuple = []
    
    li[0] = ',' + li[0]

    for i in li:
        s = i[2:]
        s_split = s.split(',')
        tmp = []
        for j in s_split:
            tmp.append(int(j))
        set_tuple.append(tmp)
    
    set_tuple.sort(key = lambda x : len(x))
    
    for i in set_tuple:
        if not answer:
            answer += i
            continue
        this = set(i)
        before = set(answer)
        answer += list(this - before)
    
    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))

'''
    1.  문자열을 리스트로 나눠준다.
    2.  리스트의 길이를 기준으로 리스트들을 오름차순으로 정렬한다.
    3.  리스트들을 순회 하며 앞의 리스트에서 추가된 원소들을 answer에 넣어준다.

    ex) 1.  "{{2,1},{2},{2,1,3},{2,1,3,4}}" -> {2,1   ,{2   ,{2,1,3    ,{2,1,3,4
            
            처음엔 }를 기준으로 split을 해주고
            리스트별로 ,{ 를 없애주었다.

        2.  2,1   2   2,1,3    2,1,3,4  ->  2    2,1   2,1,3    2,1,3,4
        리스트들을 길이 순대로 정렬하였다


        3.  2,1 에서 앞의 리스트 2를 볼 때 1이 추가 되었으므로 answer = [2,1(추가)]
            2,1,3에서 앞의 리스트 2,1을 볼 때 3이 추가 되었으므로 answer = [2,1,3(추가)]
            
        
        리스트를 순회하며 앞의 리스트와 비교하여 추가된 원소들을 답에 넣어준다.

'''