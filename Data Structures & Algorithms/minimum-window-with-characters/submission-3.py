class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        t_chars = defaultdict(int)
        for ch in t:
            t_chars[ch] += 1

        window_chars = defaultdict(int)
        res = [-1, -1]
        resLen = float('inf')
        i = 0
        j = 0
        need = len(t_chars)
        have = 0
        while j < len(s):
            window_chars[s[j]] += 1
            if s[j] in t_chars and window_chars[s[j]] == t_chars[s[j]]:
                have += 1
            while need == have:
                if j - i + 1 < resLen:
                    res = [i, j]
                    resLen = j - i + 1
                window_chars[s[i]] -= 1
                if s[i] in t_chars and window_chars[s[i]] < t_chars[s[i]]:
                    have -= 1
                i += 1
            j += 1
        i, j = res
        return s[i : j + 1] if resLen != float('inf') else ""
        