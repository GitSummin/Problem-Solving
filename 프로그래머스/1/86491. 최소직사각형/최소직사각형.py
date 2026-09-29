def solution(sizes):
    max_width = 0
    max_height = 0
    
    for w, h in sizes:
        max_width = max(max_width, max(w, h))
        max_height = max(max_height, min(w, h))
    
    return max_width * max_height