

def solution(numbers):
    s1 = set()
    for i in range(0,len(numbers)):
        for j in range(i+1,len(numbers)):
            s1.add(number[i]+numbers[j])
    
    answer =list(s1)
    answer.sort()

    return answer
'''
numbers = [1,2,3]
s1=set()
s1.add(1)
print(s1)
'''