def solution(info, n, m):
    INF = float('inf')

    # dp[b] = B의 흔적이 b일 때, A의 최소 흔적
    dp = [INF] * m
    dp[0] = 0

    for a, b in info:
        next_dp = [INF] * m
        
        for b_sum in range(m):
            if dp[b_sum] == INF:
                continue

            # 1. A가 물건을 훔치는 경우
            if dp[b_sum] + a < n:
                next_dp[b_sum] = min(next_dp[b_sum], dp[b_sum] + a)
            # 2. B가 물건을 훔치는 경우
            if b_sum + b < m:
                next_dp[b_sum + b] = min(next_dp[b_sum + b], dp[b_sum])

        dp = next_dp
    answer = min(dp)

    return -1 if answer == INF else answer