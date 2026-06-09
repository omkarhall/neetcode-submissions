class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l = [[strs[0]]]
        
        d = {}
        for s in strs:
            d[s] = {}
            for ch in s:
                if ch in d[s]:
                    d[s][ch] += 1
                else:
                    d[s][ch] = 1
        added = False
        for i in range(1, len(strs)):
            for j in range(len(l)):
                if d[strs[i]] == d[l[j][0]]:
                    l[j].append(strs[i])
                    added = True
                    break
            if not added:
                l.append([strs[i]])
            added = False
        return l
                