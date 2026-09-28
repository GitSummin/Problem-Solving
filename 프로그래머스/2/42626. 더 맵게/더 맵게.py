import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) # 최소 힙 구조 생성
    
    while scoville[0] < K: # 가장 작은 스코빌 값이 K보다 작은 동안 계속 섞음
        if len(scoville) < 2:
            return -1
        
        first = heapq.heappop(scoville) # 최소값 제거
        second = heapq.heappop(scoville) # 다음 최소값 제거
        
        mixed = first + second * 2
        
        heapq.heappush(scoville, mixed) # mixed 값을 최소 힙에 다시 추가
        
        answer += 1
    
    return answer