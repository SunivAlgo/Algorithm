def solution(msg):
    answer, cnt, i = [], 27, 0
    dic = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

    while i<len(msg):
        s=msg[i]
        tmp = dic[s]
        while(True):
            if s in dic:
                tmp = dic[s]
                i=i+1
                if i==len(msg):
                    answer.append(tmp)
                    break
                s+=msg[i]
            else:
                dic[s]=cnt
                cnt+=1
                answer.append(tmp)
                break

    return answer

# https://blog.naver.com/leemyo_/222274126477