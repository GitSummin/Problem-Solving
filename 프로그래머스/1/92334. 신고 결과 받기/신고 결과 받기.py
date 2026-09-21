def solution(id_list, report, k):
    answer = []
    
    report = set(report)
    
    recieve_dict = {}
    mail_dict = {}
    
    for id in id_list:
        recieve_dict[id] = 0
        mail_dict[id] = 0
        
    for _ in report:
        send, recieve = _.split()
        recieve_dict[recieve] += 1
    
    for _ in report:
        send, recieve = _.split()
        if recieve_dict[recieve] >= k:
            mail_dict[send] += 1
    
    answer = [mail_dict[id] for id in id_list]
    
    return answer