from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    for order in permutations(dungeons):
        # 각 던전 순서마다 처음 피로도부터 다시 시작
        current_k = k
        count = 0
        
        for value in order:
            need, cost = value
            
            if current_k >= need:
                current_k -= cost
                count += 1
            else:
                break

        # 현재 순서에서 탐험한 던전 수와 최댓값 비교
        answer = max(answer, count)
    
    return answer