def solution(nums):
    answer = 0
    
    target_len = int(len(nums) / 2)
    stack = [] * target_len
    
    for num in nums:
        if (not num in stack):
            if len(stack) < target_len:
                stack.append(num)
            else:
                break
            
    answer = max(answer, len(stack))
    
    return answer