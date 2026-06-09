class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lk = 1
        rk = max(piles)
        validk = max(piles)
        while lk <= rk:
            hours = 0
            midk = (lk + rk) // 2
            for p in piles:
                hours += math.ceil(p / midk)
            if hours > h:
                lk = midk + 1
            elif hours <= h:
                validk = midk
                rk = midk - 1
        return validk
            
            