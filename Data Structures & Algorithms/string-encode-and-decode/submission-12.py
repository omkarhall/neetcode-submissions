class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)) + "#" + s)
        return "".join(res)
    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            read = int(s[i:j])
            res.append(s[j+1:j+read+1])
            i = j + read + 1
            '''
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
            '''
        return res