
def solution(genres, plays):
    answer = []
    dic_gen = dict() ## 장르 딕셔너리
    dic_gen_count = dict() ## 장르 총 횟수 딕셔너리
    index = 0

    for g,p in zip(genres,plays):
        if g not in dic_gen:
            dic_gen[g] = [[p,index]]
            dic_gen_count[g] = p
        else:
            dic_gen[g].append([p,index])
            dic_gen[g].sort(key = lambda x : x[0], reverse = True)
            dic_gen_count[g] += p
        index += 1
    
    ## 장르 count의 key, value를 묶은 리스트를 내림차순으로 정렬해서 dic_gen_count는 2차원 리스트가 됨
    dic_gen_count = sorted(list(zip(dic_gen_count.keys(),dic_gen_count.values())), key= lambda x: x[1], reverse= True)
    
    for g in dic_gen_count:
        answer.append(dic_gen[g[0]][0][1])
        if len(dic_gen[g[0]]) >= 2:
            answer.append(dic_gen[g[0]][1][1])


    return answer