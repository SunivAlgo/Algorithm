
def solution(phone_book):
    answer = True
    for i in phone_book:
        s = ""
        for j in range (0, len(i)-1):
            s += i[j]
            if s in phone_book: 
                return False

    return answer

phone_book = ["119", "97674223", "1195524421"]
solution(phone_book)

'''
각각의 문자열의 문자들을 처음부터 끝까지 하나씩 붙여주면서
리스트에 해당 문자열이 있는지 확인했다.
리스트에서 확인하는것 대신 해쉬맵을 하나 만들어서 쓰면
더 빠를거 같긴하다.
''' 