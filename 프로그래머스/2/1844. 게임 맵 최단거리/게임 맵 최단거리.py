def solution(maps):
    n = len(maps)
    m = len(maps[0])

    queue = [(0, 0)]
    head = 0

    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    while head < len(queue):
        x, y = queue[head]
        head += 1

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            if not (0 <= nx < n and 0 <= ny < m):
                continue

            # 시작점 재방문 방지
            if (nx, ny) == (0, 0):
                continue

            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))

    if maps[n - 1][m - 1] == 1:
        return -1

    return maps[n - 1][m - 1]