def solution(name):
    answer = 0
    n = len(name)

    # 1. 위/아래 알파벳 변경 횟수
    for alpha in name:
        up = ord(alpha) - ord('A')
        down = ord('Z') - ord(alpha) + 1

        answer += min(up, down)

    # 2. 좌/우 커서 이동
    move = n - 1

    for i in range(n):
        next_idx = i + 1

        # i 다음부터 연속된 A를 건너뜀
        while next_idx < n and name[next_idx] == 'A':
            next_idx += 1

        # 오른쪽으로 갔다가 되돌아오는 경우
        move = min(move, 2 * i + n - next_idx, i + 2 * (n - next_idx))

    return answer + move