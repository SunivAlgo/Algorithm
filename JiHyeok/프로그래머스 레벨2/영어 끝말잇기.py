def solution(n, words):
    answer = []

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    li = []
    for word in words:
        if not li:
            li.append(word)
            continue
        if word in li or li[-1][-1] != word[0]:
            who = len(li) % n + 1
            turn = len(li) // n + 1
            answer = [who,turn]
            break
        li.append(word)
    else:
        answer = [0,0]    

    return answer

print(solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))

'''
    1.  words에 들어있는 문자열들을 li 리스트에 옮기면서
    
    2.  li 리스트에 원래 있는 문자열 or 마지막문자열의 마지막문자와 다르면
        누가, 몇번째턴에 탈락했는지 answer

    3.  다 해당하지 않는다면 그대로 li 리스트에 넣기
'''