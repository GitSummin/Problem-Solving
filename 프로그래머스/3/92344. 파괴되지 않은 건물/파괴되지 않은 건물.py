def solution(board, skill):
    n, m = len(board), len(board[0])
    diff = [[0] * (m + 1) for _ in range(n + 1)]

    for kind, r1, c1, r2, c2, degree in skill:
        delta = -degree if kind == 1 else degree

        diff[r1][c1] += delta         # 직사각형의 시작
        diff[r1][c2 + 1] -= delta     # 오른쪽으로 넘어가는 효과를 상쇄
        diff[r2 + 1][c1] -= delta     # 아래로 넘어가는 효과를 상쇄
        diff[r2 + 1][c2 + 1] += delta # 오른쪽 아래에서 두 번 상쇄된 효과를 보정

    # 가로 누적합
    for r in range(n):
        for c in range(1, m):
            diff[r][c] += diff[r][c - 1]

    # 세로 누적합
    for r in range(1, n):
        for c in range(m):
            diff[r][c] += diff[r - 1][c]

    answer = 0
    for r in range(n):
        for c in range(m):
            if board[r][c] + diff[r][c] > 0:
                answer += 1

    return answer