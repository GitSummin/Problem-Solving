def solution(n, results):
    win = [[False] * (n+1) for _ in range(n+1)]
    
    for winner, loser in results:
        win[winner][loser] = True
    
    for via in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if win[i][via] and win[via][j]:
                    win[i][j] = True
    
    answer = 0
    for i in range(1, n+1):
        knwon = 0
        for j in range(1, n+1):
            if i != j and (win[i][j] or win[j][i]):
                knwon += 1
        if knwon == n-1:
            answer += 1
            
    return answer