def solution(routes):
    answer = 0
    
    routes.sort(key=lambda x: x[1])
    camera = -float('inf')
    
    for start, end in routes: 
        if camera < start: # 현재 카메라(camera)가 차량의 진입(start) 지점보다 더 왼쪽에 있으면 그 차량의 경로 안에 카메라가 없다
            camera = end # 새 카메라(camera)는 현재 차량의 진출(end) 지점에 설치
            answer += 1
    
    return answer

# [진입 지점, 나간 지점]