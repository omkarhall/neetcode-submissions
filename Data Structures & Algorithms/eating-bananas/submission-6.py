class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1
        hi = max(piles)
        mink = hi
        while lo <= hi:
            k = (lo + hi) // 2
            time = 0

            for p in piles:
                time += math.ceil(float(p) / k)
            
            if time <= h:
                mink = k
                hi = k - 1
            else:
                lo = k + 1
        return mink