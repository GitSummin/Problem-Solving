def solution(n, wires):
    answer = n # 송전탑 개수 (초기화)
    
    for cut in range(len(wires)):
        graph = [[] for _ in range(n+1)] # 송전탑 연결 관계를 저장할 그래프 - 송전탑 번호: 1~n (n+1 지정 이유)
        
        for i, (a, b) in enumerate(wires): # 모든 전선을 하나씩 확인
            if i == cut: # 현재 끊기로 한 전선은 그래프에 넣지 않음
                continue
            graph[a].append(b) # 양방향 전선 연결
            graph[b].append(a) # //
            
        visited = [False] * (n+1)
        queue = [1] # 1번 송전탑에서 시작 (start=1)
        head = 0
        visited[1] = True
        count = 1 # 이미 송전탑 하나를 방문했기 때문에
        
        while head < len(queue):
            current = queue[head]
            head += 1
            
            for next_node in graph[current]: # 현재 송전탑과 직접 연결된 송전탑들을 확인
                if not visited[next_node]:
                    visited[next_node] = True
                    queue.append(next_node)
                    count += 1
            
        difference = abs(count - (n-count))
        answer = min(answer, difference)
            
    return answer