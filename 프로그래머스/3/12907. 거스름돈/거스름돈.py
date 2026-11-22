def solution(n, money):    
    dp = [0] * (n+1)
    dp[0] = 1
    
    for coin in money:
        for x in range(coin, n+1):
            dp[x] = (dp[x] + dp[x - coin]) % 1000000007
    
    return dp[n]