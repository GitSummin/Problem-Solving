def solution(clothes):
    answer = 1
    cloth_dict = {}
    
    for cloth in clothes:
        item, op = cloth
        if not op in cloth_dict:
            cloth_dict[op] = [item]
        else:
            cloth_dict[op].append(item)
    
    for op in cloth_dict:
        answer *= len(cloth_dict[op]) + 1
        # 해당 종류의 옷을 안 입는 경우 +1
    
    # 아무 옷도 안 입는 경우 제외
    return answer - 1