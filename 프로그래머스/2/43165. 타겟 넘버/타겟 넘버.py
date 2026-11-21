def solution(numbers, target):
    
    def dfs(i, total):
        if i == len(numbers):
            if total == target:
                return 1
            return 0
        
        num = numbers[i]
        plus = dfs(i+1, total + num)
        minus = dfs(i+1, total - num)
        
        return plus + minus
    
    return dfs(0,0)