def solution(board):
    n, m = len(board), len(board[0])
    dp = [[0]*(m+1) for _ in range(n+1)] 
    max_side = 0
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                dp[i+1][j+1] = 1 + min(
                    dp[i][j+1], # 위
                    dp[i+1][j], # 왼쪽
                    dp[i][j],   # 왼쪽 위
                )
                max_side = max(max_side, dp[i+1][j+1])
    
    return max_side ** 2