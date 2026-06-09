class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)) + "#" + s)
        return "".join(res)
    def decode(self, s: str) -> List[str]:
        print(s)
        i = 0
        res = []
        while i < len(s):
            read = ""
            while s[i] != "#":
                read += s[i]
                i += 1
            i += 1
            temp = ""
            for j in range(i, i + int(read)):
                temp += s[j]
                i += 1
            res.append(temp)
        return res