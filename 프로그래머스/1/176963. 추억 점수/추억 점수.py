def solution(name, yearning, photo):
    answer = []
    score_dict = {}
    cal = 0
    
    for i in range(len(name)):
        person = name[i]
        score = yearning[i]
        score_dict[person] = score
    
    for row in photo:
        for cell in row:
            if cell in score_dict:
                cal += score_dict[cell]
        answer.append(cal)
        cal = 0
    
    return answer