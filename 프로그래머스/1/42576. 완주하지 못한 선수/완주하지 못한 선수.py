def solution(participant, completion):
    count = {}
    
    for person in participant:
        count[person] = count.get(person, 0) + 1
    
    for person in completion:
        count[person] -= 1
    
    for person in count:
        if count[person] > 0:
            return person