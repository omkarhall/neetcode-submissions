class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_cnt = defaultdict(int)
        maxHeap = [] # -num of tasks, task
        q = deque() # -num of tasks, time ready

        for t in tasks:
            task_cnt[t] += 1 
        for t in task_cnt:
            maxHeap.append(-task_cnt[t])
        
        heapq.heapify(maxHeap)
        time = 0

        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1]
            else:
                cnt = heapq.heappop(maxHeap) + 1
                if cnt < 0:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
                
        return time