def solution(clothes):
    answer = 1
    dic = {}
    
    for cloth in clothes:
        item, op = cloth
        if not op in dic:
            dic[op] = [item]
        else:
            dic[op].append(item)
    
    for op in dic:
        answer *= len(dic[op]) + 1
    
    return answer - 1