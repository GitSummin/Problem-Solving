def solution(n, costs):
    answer = 0
    parent = [i for i in range(n)]
        
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(a, b):
        a = find(a)
        b = find(b)
        
        if a != b:
            parent[b] = a
            return True
        return False
    
    costs.sort(key=lambda x: x[2])
    count = 0
    
    for island1, island2, cost in costs:
        if union(island1, island2):
            answer += cost
            count += 1
        if count == n-1:
            break
    
    return answer