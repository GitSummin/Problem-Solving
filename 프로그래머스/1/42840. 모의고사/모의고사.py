def solution(answers):
    count = [0, 0, 0]
    
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i in range(len(answers)):
        if answers[i] == first[i % len(first)]:
            count[0] += 1
        if answers[i] == second[i % len(second)]:
            count[1] += 1
        if answers[i] == third[i % len(third)]:
            count[2] += 1
    
    max_count = max(count)
    
    result = []
    
    for i in range(3):
        if count[i] == max_count:
            result.append(i + 1)
    
    return result