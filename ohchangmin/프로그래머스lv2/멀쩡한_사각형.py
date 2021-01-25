from math import gcd

def solution(w,h):  
    return w * h - (w + h - gcd(w, h))

print(solution(8,12))

"""
최대 공약수 or 최대 공배수를 활용하여
값을 구할 수 있다는 것을 알고 있었다.
그를 바탕으로 여러 방법을 대입해 보며
규칙성을 찾아내었다.
"""