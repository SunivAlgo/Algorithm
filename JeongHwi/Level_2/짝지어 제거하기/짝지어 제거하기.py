def solution(s):
    st = []
    for i in s:
        if not st:
            st.append(i)
        elif st:
            if st[-1] == i:
                st.pop()
            else:
                st.append(i)
    if st:
        return 0
    return 1    





print(solution("baabaa"))
print(solution("cdcd"))
print(solution("abccba"))
print(solution("abcccba"))
print(solution("abccccbaaa"))
print(solution("abccaabaa"))
print(solution("a"))
print(solution("abccaeeaba"))