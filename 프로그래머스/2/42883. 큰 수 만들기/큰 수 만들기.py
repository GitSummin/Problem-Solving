def solution(number, k):
    answer = ''
    stack = []
    
    for num in number:
        while k > 0 and stack and stack[-1] < num: 
            # 아직 삭제 횟수가 남아 있고, 앞에 있는 숫자가 지금 들어온 숫자보다 작다면,
            stack.pop() # 앞의 작은 숫자를 지워버린다.
            k -= 1
        stack.append(num)
        
    if k > 0:
        stack = stack[:-k]
    
    return ''.join(stack)