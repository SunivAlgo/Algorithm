def solution(str1, str2):
    answer = 0
    dict_str1 = dict() ##    str1에서 만든 두글자 단어들을 key, count값을 value로 하는 딕셔너리
    dict_str2 = dict() ##    str2에서 만든 두글자 단어들을 key, count값을 value로 하는 딕셔너리
    str1 = str1.upper() ##    소,대문자 구분이 없으므로 모두 대문자로 변형시켜 버렸음   
    str2 = str2.upper()
    
    if str1 == str2: ### 만약 문자열이 똑같으면 더이상 진행할 필요 x
        return 1 * 65536

    for i in range(len(str1) - 1): ##   dict_str1을 만드는 과정    
        s1 = str1[i]
        s2 = str1[i + 1]
        if 'A' <= s1 <= 'Z' and 'A' <= s2 <= 'Z': ##    알파벳만 처리
            s = s1 + s2
            if s not in dict_str1: 
                dict_str1[s] = 1
                continue
            dict_str1[s] += 1


    for i in range(len(str2) - 1): ##   dict_str2을 만드는 과정
        s1 = str2[i]
        s2 = str2[i + 1]
        if 'A' <= s1 <= 'Z' and 'A' <= s2 <= 'Z':
            s = s1 + s2
            if s not in dict_str2:
                dict_str2[s] = 1
                continue
            dict_str2[s] += 1
    

    set_str1_keys = set(dict_str1.keys()) ##    str1의 key들의 집합
    set_str2_keys = set(dict_str2.keys()) ##    str2의 key들의 집합
    set_for_intersection = set_str1_keys.intersection(set_str2_keys) ## dict_str1.key 와 dict_str2.key의 교집합
    set_for_union = set_str1_keys.union(set_str2_keys) ## str1.key 와 str2.key의 합집합

    
    
    intersection_count = 0 
    ##  교집합의 key들은 dict_str1,dict_str2에 모두 있으므로 둘다 검색해서 작은것을 count로 세어주면 된다.
    for i in list(set_for_intersection):
        intersection_count += min(dict_str1[i],dict_str2[i])
    
    union_count = 0
    ##  합집합의 key들은 dict_str1,dict_str2에 모두 있을수도 있고 아닐수도있으므로 경우를 다 따져서 count
    for i in list(set_for_union):
        if i in dict_str1 and i in dict_str2:
            union_count += max(dict_str1[i],dict_str2[i])
        elif i in dict_str1:
            union_count += dict_str1[i]
        elif i in dict_str2:
            union_count += dict_str2[i]
        
    return int(intersection_count / union_count * 65536)

print(solution('aa1+aa2','AAAA12'))
