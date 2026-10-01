from collections import Counter

def solution(str1, str2):
    new_str1 = []
    new_str2 = []
    
    # str1 두 글자씩 자르기
    for i in range(len(str1) - 1):
        value = str1[i:i+2]
        
        if value.isalpha():
            new_str1.append(value.lower())
    
    # str2 두 글자씩 자르기
    for i in range(len(str2) - 1):
        value = str2[i:i+2]
        
        if value.isalpha():
            new_str2.append(value.lower())
    
    count1 = Counter(new_str1)
    count2 = Counter(new_str2)
    
    intersection = count1 & count2
    union = count1 | count2
    
    intersection_count = sum(intersection.values())
    union_count = sum(union.values())
    
    # 둘 다 공집합이면 자카드 유사도 = 1
    if union_count == 0:
        return 65536
    
    similarity = intersection_count / union_count
    
    return int(similarity * 65536)