class Solution:

    def __init__(self, w: List[int]):
        #self.w = w
        wSum = sum(w)
        for i in range(len(w)):
            w[i] /=wSum 
        for i in range(1, len(w)):
            w[i] += w[i-1]
        self.w = w
        
        
    def pickIndex(self) -> int:
        pick = random.uniform(0,1)
        l, r = 0, len(self.w)-1
        
        while l <= r:
            m = (l + r)//2
            if self.w[m] == pick: return m
            elif self.w[m]> pick: r = m-1
            else: l = m+1
        return l
