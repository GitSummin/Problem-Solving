def solution(numbers):
    answer = ''
    str_numbers = []
    
    for num in numbers:
        str_numbers.append(str(num))
    str_numbers.sort(key=lambda x: x*3, reverse=True)
    
    answer = ''.join(str_numbers)
    
    if answer[0] == '0':
        return '0'
    
    return answer