class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(t) > len(s):
            return ""

        def valid(d1, d2):
            for k in d1:
                if k not in d2 or d2[k] < d1[k]:
                    return False
            return True
        
        t_chars = defaultdict(int)
        for ch in t:
            t_chars[ch] += 1

        window_chars = defaultdict(int)
        res = ""
        len_ = float('inf')
        i = 0
        j = 0
        while j < len(s):
            window_chars[s[j]] += 1
            while valid(t_chars, window_chars):
                if j - i + 1 < len_:
                    res = s[i : j + 1]
                    len_ = len(res)
                window_chars[s[i]] -= 1
                i += 1
            j += 1
        return res
        