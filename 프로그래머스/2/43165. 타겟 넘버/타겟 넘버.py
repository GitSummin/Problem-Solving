def solution(numbers, target):
    
    def dfs(index, current_sum):
        if index == len(numbers): # DFS 종료 조건: 모든 숫자를 다 사용
            if current_sum == target: # 그때 현재 합이 target이면 1
                return 1
            return 0 # 아니면 0
        
        plus = dfs(index + 1, current_sum + numbers[index])
        minus = dfs(index + 1, current_sum - numbers[index])
        
        return plus + minus
    
    return dfs(0, 0)