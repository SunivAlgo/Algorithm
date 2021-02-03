
def solution(citations):
    answer = 0
    count = 0
    citations.sort(reverse = True)
    print(citations)
    for i in citations :
        count += 1
        if count >= i:
            if count == i:
                return count
            else :
                return count - 1
            break
    return count
print(solution([2]))
'''
    1.  예를 들어 7,9,6,4,1 이란 리스트가 들어왔다. 먼저 내림차순으로 정렬. i -> 9 7 6 4 1
    2.  count 를 1씩 늘려가며 오른쪽으로 진행. 그러다 i <= count 가 되는 순간 stop
    3.  i :     9 7 6 4 1
        count : 1 2 3 4
        인 상태에서 count의 4가 의미하는 것은 i값 보다 높거나 같은 숫자가 4개 있다는 뜻.

        i == count 이면 count 그대로 return
        i < count 이면 count -1 을 해줘야 한다.
        
        i :     9 8 7 1
        count : 1 2 3 4
        인 경우 3을 출력해야 하므로.

        원소가 하나일 때는 count += 1이 한번만 적용 되어 1 출력.




    인데

    애초에 리스트를 내림차순으로 정렬시키기보다는 오름차순을 정렬하여 계산하는것이 더 편하다는 것을 찾음
     i :         1 7 8 9
     L - index : 4 3

     i :         1 4 6 7 9
     L - index : 5 4 

     에서 index = 1 일때 바로 3, 4 가 출력 될 수 있기 때문. 


    
'''