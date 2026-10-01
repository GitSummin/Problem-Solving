def solution(board):    
    n = len(board)
    m = len(board[0])
    
    visited = [[-1] * m for _ in range(n)]    
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == "R":
                x, y = i, j
    
    queue = [(x, y)]
    head = 0
    visited[x][y] = 0
    
    while head < len(queue):
        x, y = queue[head]
        head += 1
        
        if board[x][y] == "G":
            return visited[x][y]
        
        for dx, dy in directions:
            nx, ny = x, y
            
            while True:
                tx = nx + dx
                ty = ny + dy
                
                if not (0 <= tx < n and 0 <= ty < m):
                    break

                if board[tx][ty] == "D":
                    break
                
                nx = tx
                ny = ty

            if visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
                    
    return -1