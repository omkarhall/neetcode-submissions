class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.l = nums
        heapq.heapify(self.l)
        while len(self.l) > k:
            heapq.heappop(self.l)
        self.k = k


    def add(self, val: int) -> int:
        heapq.heappush(self.l, val)
        if len(self.l) > self.k:
            heapq.heappop(self.l)
        return self.l[0]
        
