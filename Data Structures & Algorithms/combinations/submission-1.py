class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def combos(i, combo):
            if i > n:
                if len(combo) == k:
                    res.append(combo.copy())
                return
            combo.append(i)
            combos(i + 1, combo)
            combo.pop()
            combos(i + 1, combo)
        combos(1, [])
        return res