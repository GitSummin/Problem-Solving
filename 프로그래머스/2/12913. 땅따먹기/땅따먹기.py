def solution(land):
    prev = land[0]
    
    for i in range(1, len(land)):
        row = land[i]
        current = [
            row[0] + max(prev[1], prev[2], prev[3]),
            row[1] + max(prev[0], prev[2], prev[3]),
            row[2] + max(prev[0], prev[1], prev[3]),
            row[3] + max(prev[0], prev[1], prev[2]),
        ]
        prev = current
    
    return max(prev)