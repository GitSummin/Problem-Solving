def solution(clothes):
    answer = 1
    clothe_dict = {}
    
    for cloth in clothes:
        item, type = cloth
        if type not in clothe_dict:
            clothe_dict[type] = [item]
        else:
            clothe_dict[type].append(item)
    
    # 각 종류마다 "(해당 종류의 의상 개수 + 아무 것도 안 입는 경우 1개)"
    for key in clothe_dict: # key 불러오는 반복문 (<-> dict.values())
        answer *= len(clothe_dict[key]) + 1
    
    # 아무것도 안 입는 경우 1개 제외
    return answer - 1