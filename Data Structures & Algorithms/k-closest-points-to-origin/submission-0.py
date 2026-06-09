class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(x1, y1):
            return math.sqrt((x1 - 0)**2 + (y1 - 0)**2)
        
        minHeap = []
        heapq.heapify(minHeap)
        for x,y in points:
            heapq.heappush(minHeap, [distance(x,y), x, y])

        res = [] 
        while k > 0:
            tup = heapq.heappop(minHeap)
            res.append([tup[1],tup[2]])
            k -= 1
        return res