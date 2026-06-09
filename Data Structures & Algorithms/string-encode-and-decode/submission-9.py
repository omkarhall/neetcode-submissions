class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)) + "#" + s)
        encoded = "".join(res)
        return encoded

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            wordlen = int(s[i:j])
            i = j
            res.append(s[i+1:i+wordlen+1])
            i = i + wordlen + 1

        return res