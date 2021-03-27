# 참조 : https://gurumee92.tistory.com/164
def solution(N,number):
    # 1~8 까지 올라가다가 되는거 있으면 바로 Return
    ans = []
    if N == number:
        return 1
    for i in range(1,9):
        numbers = set([int(str(N)*i)])
        for j in range(0,i-1):
            for x in ans[j]:
                for y in ans[-j-1]:
                    print(ans[j],ans[-j-1],i,"\n",x,y)
                    print("=============")
                    numbers.add(x+y)
                    numbers.add(x-y)
                    numbers.add(x*y)
                    if y!= 0:
                        numbers.add(x//y)
        if number in numbers:
            return i
        
        ans.append(numbers)
        # print(ans)
    return -1

print(solution(5,12))
# print(solution(1,1121),7)
# print(solution(5,1010),7)
# print(solution(5,5555),4)