def solution(dirs):
    answer = 0
    
    directions = {
        'U': (0, 1),
        'D': (0, -1),
        'R': (1, 0),
        'L': (-1, 0)
    }
    
    x, y = 0, 0
    visited = set()
    
    for op in dirs:
        dx, dy = directions[op]
        nx = x + dx
        ny = y + dy
        
        # 좌표 범위를 벗어나면 이동하지 않음
        if not (-5 <= nx <= 5 and -5 <= ny <= 5):
            continue
        
        # 현재 위치 -> 다음 위치
        path = ((x, y), (nx, ny))
        reverse_path = ((nx, ny), (x, y))
        
        # 처음 지나가는 길이면 카운트
        if path not in visited:
            visited.add(path)
            visited.add(reverse_path)
            answer += 1
        
        # 실제 위치 이동
        x, y = nx, ny
    
    return answer