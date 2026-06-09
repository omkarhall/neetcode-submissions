class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for n in nums:
            d[n] += 1
        l = []
        for i in range(k):
            maxKey = max(d, key=d.get)
            l.append(maxKey)
            d[maxKey] = 0
        return l