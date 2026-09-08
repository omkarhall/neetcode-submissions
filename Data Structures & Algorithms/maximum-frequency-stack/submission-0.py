class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int)
        self.maxCnt = 0
        self.cnts = defaultdict(list)

    def push(self, val: int) -> None:
        self.freq[val] += 1
        self.maxCnt = max(self.maxCnt, self.freq[val])
        self.cnts[self.freq[val]].append(val)

    def pop(self) -> int:
        val = self.cnts[self.maxCnt].pop()
        self.freq[val] -= 1
        if not self.cnts[self.maxCnt]:
            self.maxCnt -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()