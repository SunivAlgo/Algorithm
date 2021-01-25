def solution(phone_number):
    answer = ''

    for i in range(0,len(phone_number)-4):
        phone_number[i] = '*'
    return answer