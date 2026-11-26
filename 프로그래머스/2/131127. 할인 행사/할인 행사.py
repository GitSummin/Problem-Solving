from collections import Counter

def solution(want, number, discount):    
    need = dict(zip(want, number))
    answer = 0
    
    for start in range(len(discount) - 10 + 1):
        window = discount[start:start+10]
        counts = Counter(window)
        
        if counts == need:
            answer += 1
    
    return answer