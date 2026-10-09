import heapq

def solution(jobs):
    jobs = [(request, run, i) for i, (request, run) in enumerate(jobs)]
    jobs.sort()

    heap = []
    current_time = 0
    index = 0
    total = 0

    while index < len(jobs) or heap:
        while index < len(jobs) and jobs[index][0] <= current_time:
            request, run, job_num = jobs[index]
            heapq.heappush(heap, (run, request, job_num))
            index += 1

        if heap:
            run, request, job_num = heapq.heappop(heap)
            current_time += run
            total += current_time - request
        else:
            current_time = jobs[index][0]

    return total // len(jobs)