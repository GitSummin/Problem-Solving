def solution(nums):
    target_len = int(len(nums) // 2)
    unique_nums = set(nums)

    return min(target_len, len(unique_nums))