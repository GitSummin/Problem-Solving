def solution(numbers, target):
    
    def dfs(i, total):
        if i == len(numbers): 
            # len(numbers)-1로 설정하면 한 턴 더 돌아야 함 (모든 숫자 사용 조건)
            if total == target:
                return 1
            return 0
        
        num = numbers[i]              # numbers[i]에
        plus = dfs(i+1, total + num)  # +를 붙인 경우 중 성공한 방법의 수 
        minus = dfs(i+1, total - num) # -를 붙인 경우 중 성공한 방법의 수
        
        return plus + minus
    
    return dfs(0,0)