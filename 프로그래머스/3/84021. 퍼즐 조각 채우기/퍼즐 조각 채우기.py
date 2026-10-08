def solution(game_board, table):
    n = len(game_board)

    directions = [(-1,0), (1,0),(0,-1),(0,1)]

    # 연결된 하나의 덩어리를 BFS로 찾는 함수
    def bfs(board, start_x, start_y, target, visited):
        queue = [(start_x, start_y)]
        head = 0
        visited[start_x][start_y] = True
        shape = []

        while head < len(queue):
            x, y = queue[head]
            head += 1
            shape.append((x, y))

            for dx, dy in directions:
                nx = x + dx
                ny = y + dy

                if not (0 <= nx < n and 0 <= ny < n):
                    continue

                if visited[nx][ny]:
                    continue

                if board[nx][ny] != target:
                    continue

                visited[nx][ny] = True
                queue.append((nx, ny))

        return normalize(shape)

    # 좌표를 (0,0) 기준으로 이동
    def normalize(shape):
        min_x = min(x for x, y in shape)
        min_y = min(y for x, y in shape)

        result = []

        for x, y in shape:
            result.append((x - min_x, y - min_y))

        return sorted(result)

    # 퍼즐 90도 회전
    def rotate(shape):
        rotated = []

        for x, y in shape:
            # (x, y) -> (y, -x)
            rotated.append((y, -x))

        return normalize(rotated)

    # board에서 target 값으로 연결된 모든 덩어리 추출
    def get_shapes(board, target):
        visited = [[False] * n for _ in range(n)]
        shapes = []

        for i in range(n):
            for j in range(n):
                if board[i][j] == target and not visited[i][j]:
                    shape = bfs(board, i, j, target, visited)
                    shapes.append(shape)
        return shapes

    # game_board의 0 영역 = 채워야 할 빈 공간
    blanks = get_shapes(game_board, 0)
    # table의 1 영역 = 퍼즐 조각
    puzzles = get_shapes(table, 1)

    used = [False] * len(puzzles)
    answer = 0

    # 빈 공간 하나씩 확인
    for blank in blanks:
        for i in range(len(puzzles)):
            if used[i]:
                continue
            puzzle = puzzles[i]
            # 칸 개수가 다르면 애초에 불가능
            if len(blank) != len(puzzle):
                continue
            current = puzzle

            # 0, 90, 180, 270도 확인
            for _ in range(4):
                if blank == current:
                    used[i] = True
                    answer += len(blank)
                    break
                current = rotate(current)

            # 이 blank에 퍼즐을 이미 넣었다면
            # 다른 퍼즐을 볼 필요 없음
            if used[i]:
                break

    return answer