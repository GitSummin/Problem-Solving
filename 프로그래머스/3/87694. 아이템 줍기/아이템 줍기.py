def solution(rectangle, characterX, characterY, itemX, itemY):
    # 좌표를 2배 했으므로 최대 100 정도 필요
    board = [[0] * 102 for _ in range(102)]

    # 1. 직사각형들을 좌표 2배 후 board에 표시
    for x1, y1, x2, y2 in rectangle:
        x1 *= 2
        y1 *= 2
        x2 *= 2
        y2 *= 2

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):

                # 직사각형 내부
                if x1 < x < x2 and y1 < y < y2:
                    board[x][y] = 2

                # 직사각형 테두리
                else:
                    # 이미 다른 직사각형의 내부라면
                    # 테두리로 다시 바꾸면 안 됨
                    if board[x][y] != 2:
                        board[x][y] = 1

    # 2. 캐릭터와 아이템 좌표도 2배
    characterX *= 2
    characterY *= 2
    itemX *= 2
    itemY *= 2

    # 3. BFS 준비
    queue = [(characterX, characterY)]
    head = 0

    visited = [[-1] * 102 for _ in range(102)]
    visited[characterX][characterY] = 0

    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    # 4. 테두리만 따라 BFS
    while head < len(queue):
        x, y = queue[head]
        head += 1

        # 아이템에 도착
        if x == itemX and y == itemY:
            return visited[x][y] // 2

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            # 범위 확인
            if not (0 <= nx < 102 and 0 <= ny < 102):
                continue

            # 테두리가 아니면 이동 불가
            if board[nx][ny] != 1:
                continue

            # 이미 방문한 곳
            if visited[nx][ny] != -1:
                continue

            visited[nx][ny] = visited[x][y] + 1
            queue.append((nx, ny))

    return 0