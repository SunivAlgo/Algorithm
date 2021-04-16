
def solution(genres,plays):
    # genres : 노래의 장르
    # plays : 노래별 재생횟수
    album = dict()

    # Album Init
    for i,song in enumerate(zip(genres,plays)):
        if song[0] not in album:
            album[song[0]] = [[i,song[1]]]
        else:
            album[song[0]].append([i,song[1]])
    
    sums = []
    # Plays Sort
    for s in album:
        album[s].sort(key=lambda x:-x[1])
        sums.append([s,sum([x[1] for x in album[s]])])
    sums.sort(key=lambda x:-x[1])
    ans = []
    for g,_ in sums:
        for i,al in enumerate(album[g]):
            if i == 2:
                break
            ans.append(al[0])
    return ans
    



print(solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500]))