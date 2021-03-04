def str_rp(m):
    m = m.replace("C#","1")
    m = m.replace("D#","2")
    m = m.replace("F#","3")
    m = m.replace("G#","4")
    m = m.replace("A#","5")
    return m

def solution(m, musicinfos):
    answer, savelen = '', 0

    for x in musicinfos:
        m_info=x.split(',')
        m_len= 60*(int(m_info[1][:2])-int(m_info[0][:2])) + (int(m_info[1][3:])-int(m_info[0][3:]))
        m = str_rp(m)
        m_info[3] = str_rp(m_info[3])

        if len(m_info[3]) > m_len:
            m_info[3] = m_info[3][:m_len]
        else:
            m_info[3] = m_info[3]*int(m_len//len(m_info[3])) + m_info[3][:(m_len%len(m_info[3]))]
        
        if m in m_info[3] and m_len > savelen:
            answer = m_info[2]
            savelen = m_len

    if savelen==0: answer="(None)"
        
    return answer

#https://blog.naver.com/leemyo_/222264785396