class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]
        
        for i in range(len(nums)):
            count[nums[i]] += 1
        
        for num, v in count.items():
            freq[v].append(num)
        
        res = []
        i = len(freq) - 1
        while k > 0 and i >= 0:
            if freq[i]:
                for val in freq[i]:
                    res.append(val)
                k -= len(freq[i])
            i -= 1
        return res
