from itertools import chain
count_one = 0
count_zero = 0
def sol(arr,length,a,b):
    global count_one,count_zero
    ### print('length : %d  a : %d  b : %d  1 = %d  0 = %d ' %(length,a,b,count_one,count_zero))
    if length == 1:
        if arr[a][b] == 0:
            count_zero += 1
            return
        else:
            count_one += 1
            return
    li = []
    
    for i in range(a , a + length):
        li += arr[i][b:b+length]
    ### print(li,'\n\n')
    
    if 0 not in li:
        count_one += 1
        return

    if 1 not in li:
        count_zero += 1
        return
    
    new_length = length//2

    sol(arr , new_length , a , b)
    sol(arr , new_length , a , b + new_length)
    sol(arr , new_length , a + new_length , b)
    sol(arr , new_length , a + new_length , b + new_length)
    
def solution(arr):
    global count_one,count_zero
    
    sol(arr,len(arr),0,0)
 
    answer = [count_zero,count_one]

    return answer


print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))
print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]))

'''
    1.  주어진 배열의 모든 원소가 0 혹은 1인지 확인한다. -> 나같은경우 1차원리스트로 만들어서 판단하였음
    2.  모두 0 이나 1 이면 해당 count를 up 시키고 그대로 종료
    3.  한변의 길이가 1이면 원소값을 확인후 count up 후 종료
    4.  2,3 에 해당하지 않을 시 4분할로 나눠서 재귀시작
'''