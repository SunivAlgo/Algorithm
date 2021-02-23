def solution(s):
    st = []
    for i in s:
        if st and st[-1] == i:
            st.pop()
        else:
            st.append(i)
    
    if st:
        return 0
    return 1

s = "baabaa"
print(solution(s))

'''
스텍사용
for문 한번만 
'''