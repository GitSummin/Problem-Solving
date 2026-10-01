def solution(new_id):    
    new_id = new_id.lower()
    lst = []
    
    for value in new_id:
        if (
            value == '-' 
            or value == '_' 
            or value == '.' 
            or value.isalpha() 
            or value.isdecimal()
        ):
            lst.append(value)
    
    i=0

    while i < len(lst) - 1:
        if lst[i] == '.' and lst[i + 1] == '.':
            del lst[i + 1]
        else:
            i += 1

    if lst and lst[0] == '.':
        del lst[0]
        
    if lst and lst[-1] == '.':
        del lst[-1]

    if len(lst) == 0: 
        lst.append('a')
        
    if len(lst) >= 16: 
        lst = lst[:15]
        
        if lst[-1] == '.': 
            del lst[-1]

    if len(lst) <= 2: 
        while len(lst) < 3:
            lst.append(lst[-1])
            
    return ''.join(lst)