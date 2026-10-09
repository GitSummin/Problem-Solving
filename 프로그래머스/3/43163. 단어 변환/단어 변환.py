def solution(begin, target, words):
    if not target in words:
        return 0
    
    visited = [False] * len(words)
    queue = [(begin, 0)]
    head = 0
    
    while head < len(queue):
        current, count = queue[head]
        head += 1
        
        if current == target:
            return count
        
        for i, word in enumerate(words):
            if visited[i]:
                continue            
            difference = 0
            
            for a, b in zip(current, word):
                if a != b:
                    difference += 1
            if difference == 1:
                queue.append((word, count+1))
                visited[i] = True
                        
    return 0