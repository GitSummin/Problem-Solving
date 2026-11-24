def solution(sequence):
    plus_ending = sequence[0]
    minus_ending = - sequence[0]
    answer = max(plus_ending, minus_ending)
    
    for i in range(1, len(sequence)):
        value = sequence[i]
        x = value if i % 2 == 0 else -value
        
        plus_ending = max(x, plus_ending + x)
        minus_ending = max(-x, minus_ending - x)
        
        answer = max(answer, plus_ending, minus_ending)
    
    return answer