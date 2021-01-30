def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)):
        for j in range(len(phone_book) - 1, i, -1):
            if phone_book[i] in phone_book[j]:
                return False
    return answer
