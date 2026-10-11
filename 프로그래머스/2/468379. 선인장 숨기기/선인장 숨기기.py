from collections import deque

def solution(m, n, h, w, drops):
    # 비가 오지 않은 칸은 모든 빗방울 이후라고 생각
    INF = len(drops) + 1

    # 각 칸에 몇 번째로 비가 떨어졌는지 저장 (2차원)
    rain = [[INF] * n for _ in range(m)]

    for time, (r, c) in enumerate(drops, 1):
        rain[r][c] = time

    # 가로 w칸짜리 구간의 최솟값 계산
    cols = n - w + 1
    row_min = [[0] * cols for _ in range(m)]

    for r in range(m):
        queue = deque()

        for c in range(n):
            # 현재 가로 구간에서 벗어난 인덱스 제거
            while queue and queue[0] <= c - w:
                queue.popleft()

            current = rain[r][c]

            # 현재 값보다 크거나 같은 값 제거
            while queue and rain[r][queue[-1]] >= current:
                queue.pop()

            queue.append(c)

            # 길이 w짜리 구간이 완성되면 최솟값 저장
            if c >= w - 1:
                start_c = c - w + 1
                row_min[r][start_c] = rain[r][queue[0]]

    # 세로 h칸에 대해서 다시 최솟값 계산
    best_time = -1
    best_r = 0
    best_c = 0

    for c in range(cols):
        queue = deque()

        for r in range(m):
            # 현재 세로 구간에서 벗어난 행 제거
            while queue and queue[0] <= r - h:
                queue.popleft()

            current = row_min[r][c]

            # 현재 값보다 크거나 같은 값 제거
            while queue and row_min[queue[-1]][c] >= current:
                queue.pop()

            queue.append(r)

            # h × w 구역이 완성되면 최솟값 확인
            if r >= h - 1:
                start_r = r - h + 1

                # 이 구역에서 가장 먼저 비가 내리는 시점
                first_rain = row_min[queue[0]][c]

                # 가장 늦게 비를 맞는 구역 선택
                if first_rain > best_time:
                    best_time = first_rain
                    best_r = start_r
                    best_c = c

                # 시간이 같으면 위쪽, 그다음 왼쪽 우선
                elif first_rain == best_time:
                    if start_r < best_r:
                        best_r = start_r
                        best_c = c
                    elif start_r == best_r and c < best_c:
                        best_c = c

    return [best_r, best_c]