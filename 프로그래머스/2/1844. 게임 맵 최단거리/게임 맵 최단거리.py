def solution(maps):    
    n = len(maps)
    m = len(maps[0])

    # 1. 시작점
    queue = [(0,0)]
    head = 0

    # 2. 상하좌우
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
        
    # 3. BFS
    while head < len(queue):
        x, y = queue[head]
        head += 1
                
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            
            # 4. 범위 체크
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            
            # 5. 이동 가능한지 + 방문 여부 체크
            if maps[nx][ny] == 1: # (이동 가능하고, 아직 방문하지 않음)
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny)) # (방문 처리)
    
    if maps[n-1][m-1] == 1:
        return -1
    
    return maps[n-1][m-1]

# 0 -> 벽
# 1 -> 갈 수 있는 길
# 2 이상 -> 방문 완료 + 거리 (해당 문제에서 visited 배열이 없어도 되는 이유)