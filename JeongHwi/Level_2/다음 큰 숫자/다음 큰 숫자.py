from collections import Counter
def solution(n):
    number = n
    nbin = list(bin(number)[2:])
    nCount = Counter(nbin)
    while True:
        number+=1
        new_bin = list(bin(number)[2:])
        newCount = Counter(new_bin)
        if nCount["1"] == newCount["1"]:
            break
    return number

print(solution(78))
print(solution(15))