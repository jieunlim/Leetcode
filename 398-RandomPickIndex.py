class Solution:

    def __init__(self, nums: List[int]):
        self.dic = defaultdict(list)
        for i, num in enumerate(nums):
            self.dic[num].append(i)

    def pick(self, target: int) -> int:
        if len(self.dic[target])==1: return self.dic[target][0]
        else:
            n = random.randrange(0, len(self.dic[target]))
            return self.dic[target][n]
