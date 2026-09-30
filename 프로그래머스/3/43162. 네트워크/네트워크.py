def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    for start in range(n): # 모든 컴퓨터 순회
        if visited[start]: # 이미 방문 컴퓨터 -> 넘어감
            continue
        answer += 1 # visited[start] == False -> 새로운 네트워크 발견 -> answer += 1

        queue = [start]
        head = 0
        visited[start] = True

        while head < len(queue):
            current = queue[head]
            head += 1

            for next_com in range(n):
                if computers[current][next_com] == 1: # 현재 컴퓨터와 연결된 컴퓨터 찾기
                    if not visited[next_com]:
                        visited[next_com] = True
                        queue.append(next_com)
                        
    return answer