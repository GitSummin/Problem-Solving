def solution(today, terms, privacies):
    answer = []
    
    def to_days(date):
        year, month, day = map(int, date.split('.'))
        return year * 12 * 28 + month * 28 + day
    
    today_days = to_days(today)
    term_dict = {}
    
    for term in terms:
        option, month = term.split()
        term_dict[option] = int(month)
        
    for i, privacy in enumerate(privacies):
        date, option = privacy.split()
        collected_days = to_days(date) + term_dict[option] * 28
        
        if today_days >= collected_days:
            answer.append(i+1)
    
    return answer