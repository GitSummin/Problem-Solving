def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    visited = [[False]*m for _ in range(n)]
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    
    head = 0
    queue = [(0,0)]
    visited[0][0] = True
        
    while head < len(queue):
        x, y = queue[head]
        head += 1
                                
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            
            if maps[nx][ny] == 0:
                continue
            
            if not visited[nx][ny]:
                visited[nx][ny] = True
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
            
    if not visited[n-1][m-1]:
        return -1
        
    return maps[n-1][m-1]