def solution(maps):
    n = len(maps)
    m = len(maps[0])

    # S, L, E 위치 찾기
    for i, row in enumerate(maps):
        for j, cell in enumerate(row):
            if cell == "S":
                start = (i, j)
            elif cell == "L":
                lever = (i, j)
            elif cell == "E":
                exit = (i, j)

    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    def bfs(start, end):
        queue = [start]
        head = 0

        visited = [[-1] * m for _ in range(n)]

        sx, sy = start
        visited[sx][sy] = 0

        while head < len(queue):
            x, y = queue[head]
            head += 1

            if (x, y) == end:
                return visited[x][y]

            for dx, dy in directions:
                nx = x + dx
                ny = y + dy

                # 맵 범위를 벗어나면 이동 불가
                if not (0 <= nx < n and 0 <= ny < m):
                    continue

                # 벽이면 이동 불가
                if maps[nx][ny] == "X":
                    continue

                # 이미 방문한 곳이면 이동하지 않음
                if visited[nx][ny] != -1:
                    continue

                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))

        return -1

    # 시작점 -> 레버
    first = bfs(start, lever)

    if first == -1:
        return -1

    # 레버 -> 출구
    second = bfs(lever, exit)

    if second == -1:
        return -1

    return first + second