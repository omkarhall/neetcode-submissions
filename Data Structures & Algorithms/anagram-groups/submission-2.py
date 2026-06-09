class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for i in range(len(strs)):
            temp = [0] * 26
            for j in range(len(strs[i])):
                temp[ord(strs[i][j]) - ord('a')] += 1
            d[tuple(temp)].append(strs[i])
        return list(d.values())