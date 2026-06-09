class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)

        for n in nums:
            d[n] += 1
        
        res = []
        while k > 0:
            m = max(d,key=d.get)
            res.append(m)
            d.pop(m)
            k -= 1
        return res
            