# [i][0] : i번째 차량이고속도로에 진입한 지점
# [i][1] : j번째 차량이 고속도로에서 나간 지점
def solution(routes):
    routes.sort(key=lambda x:x[1])
    ans = 0
    camera = 0
    for i,inout in enumerate(routes):
        if i == 0:
            camera = inout[1]
            ans += 1
            continue
        if not(inout[0] <= camera <= inout[1]):
            camera = inout[1]
            ans+=1
            continue
    return ans

# 1번째는 가장 먼저 나간 곳에 설치해야 첫차를 검사할 수 있다.
# 2번째 이후로는 현재의 카메라가 진입 진출 사이에 없다면
# 진출하는 시간대에 카메라를 세워두면 가장 그 전에 들어오는
# 차를 검사할 수 있따.

print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))