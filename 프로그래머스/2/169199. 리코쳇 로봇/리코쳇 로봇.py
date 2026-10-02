def solution(board):    
    n = len(board)
    m = len(board[0])
    
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    visited = [[-1]*m for _ in range(n)]
    
    for i, row in enumerate(board):
        for j, cell in enumerate(board[i]):
            if cell == "R":
                x, y = i, j
                
    queue = [(x, y)]
    head = 0
    visited[x][y] = 0
    
    while head < len(queue):
        x, y = queue[head]
        head += 1

        # 현재 멈춘 위치가 목표면 종료
        if board[x][y] == "G":
            return visited[x][y]

        # 상하좌우 각각 시도
        for dx, dy in directions:
            nx, ny = x, y

            # 한 방향으로 끝까지 미끄러지기
            while True:
                tx = nx + dx
                ty = ny + dy
                
                # 다음 칸이 보드 밖이면 현재 위치에서 정지
                if not (0 <= tx < n and 0 <= ty < m):
                    break

                # 다음 칸이 장애물이면 현재 위치에서 정지
                if board[tx][ty] == "D":
                    break
                
                # 이동 가능
                nx, ny = tx, ty
                
            # 최종 정지 위치가 미방문이면 BFS에 추가
            if visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
    
    return -1