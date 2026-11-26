def solution(elements):
    n = len(elements)
    doubled = elements + elements
    sums = set()
        
    for start in range(n):
        total = 0
        for end in range(start, start+n): # 원형수열의 성질 반영 범위
            total += doubled[end]
            sums.add(total)
                
    return len(sums)