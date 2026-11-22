def solution(sticker):
    n = len(sticker)
    if n == 1:
        return sticker[0]
    
    def max_sum(start, end):
        prev_two = 0 # 두 칸 전까지의 최대 합
        prev_one = 0 # 한 칸 전까지의 최대 합
        
        for i in range(start, end):
            skip = prev_one
            take = prev_two + sticker[i]
            current = max(skip, take)
            prev_two, prev_one = prev_one, current
        
        return prev_one
    
    return max(max_sum(0, n-1), max_sum(1, n))