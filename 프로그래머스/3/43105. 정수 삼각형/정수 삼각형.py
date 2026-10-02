def solution(triangle):
    dp = []
    dp.append([triangle[0][0]])

    for i in range(1, len(triangle)):
        row = []
        
        for j in range(len(triangle[i])):
            
            # 왼쪽 끝
            if j == 0:
                value = triangle[i][j] + dp[i-1][j]

            # 오른쪽 끝
            elif j == i:
                value = triangle[i][j] + dp[i-1][j-1]

            # 가운데
            else:
                value = triangle[i][j] + max(
                    dp[i-1][j-1],
                    dp[i-1][j]
                )

            row.append(value)

        dp.append(row)
    
    return max(dp[-1])