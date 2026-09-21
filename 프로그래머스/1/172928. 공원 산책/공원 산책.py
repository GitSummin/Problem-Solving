def solution(park, routes):
    
    H = len(park)
    W = len(park[0])
    
    for i, row in enumerate(park):
        for j, cell in enumerate(park[i]):
            if cell == "S":
                x,y = i, j
            
    direction = {
        'N': (-1, 0),
        'S': (1, 0),
        'W': (0, -1),
        'E': (0, 1)
    }
    
    for route in routes:
        op, n = route.split()
        n = int(n)
        
        nx, ny = x, y
        dx, dy = direction[op]
        
        possible = True
        
        for _ in range(n):
            nx += dx
            ny += dy
            
            if not (0 <= nx < H and 0 <= ny < W):
                possible = False
                break
            if park[nx][ny] == "X":
                possible = False
                break
        if possible:
            x, y = nx, ny
    
    return [x, y]