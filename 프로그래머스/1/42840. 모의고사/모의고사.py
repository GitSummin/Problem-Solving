def solution(answers):
    result = []
    
    first = [1, 2, 3, 4, 5] 
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    score = [0,0,0]
    
    for i, answer in enumerate(answers):
        if first[i % len(first)] == answer:
            score[0] += 1
        if second[i % len(second)] == answer:
            score[1] += 1            
        if third[i % len(third)] == answer:
            score[2] += 1
    
    for i, person in enumerate(score):
        if person == max(score):
            result.append(i+1)
            
    return result