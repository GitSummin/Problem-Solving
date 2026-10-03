def solution(nums):
    target_len = int(len(nums) // 2)
    stack = [] * target_len
    
    for num in nums:
        if (not num in stack) and len(stack) < target_len:
            stack.append(num)
        
    return len(stack)