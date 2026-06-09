class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-stone for stone in stones]
        heapq.heapify(maxheap)

        while maxheap:
            if len(maxheap) == 1:
                return -1 * heapq.heappop(maxheap)

            x = -1 * heapq.heappop(maxheap)
            y = -1 * heapq.heappop(maxheap)

            if y < x:
                n = -1 * (x-y)
                heapq.heappush(maxheap, n)
        return 0