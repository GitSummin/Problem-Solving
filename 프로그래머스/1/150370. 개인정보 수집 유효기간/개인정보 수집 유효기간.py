def solution(today, terms, privacies):
    answer = []
    
    def to_days(date):
        year, month, day = map(int, date.split('.'))
        return year * 12 * 28 + month * 28 + day
    
    today_days = to_days(today)
    
    month_dict = {}
    for term in terms:
        op, month = term.split()
        month = int(month)
        month_dict[op] = month

    for i, privacy in enumerate(privacies):
        collected, op = privacy.split()
        collected_days = to_days(collected) + month_dict[op] * 28
        
        if today_days >= collected_days:
            answer.append(i+1)
    
    return answer