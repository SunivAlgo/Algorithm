def make_N(i, n):
    str_n = ''
    dic={0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'A',
         11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    while(True):
        str_n+=dic[i%n]
        i //= n
        if i==0: break
    return ''.join(reversed(str_n))

def solution(n, t, m, p):
    answer, a = '', ''
    maxlen = t*m+p
    for i in range(maxlen+1):
        a+=make_N(i, n)
        if len(a) > maxlen: break
    for cnt in range(t):
        answer+=a[cnt*m+p-1]

    return answer

# https://blog.naver.com/leemyo_/222271508150