class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        taps = 0
        jumps = [-1] * n
        for i, num in enumerate(ranges):
            if num == 0: continue
            l = max(0, i - num)
            r = min(n, i + num)
            
            jumps[l] = max(jumps[l], r)
        print(jumps)
        curr = 0
        end = -1
        # 0  1  2   3   4
        #[5, 3, 4, -1, -1]

        for i, r in enumerate(jumps):
            end = max(end, r)
            if i == curr:
                if r == -1 and end <= i:
                    return -1
                curr = end
                taps += 1
        if end == n:
            return taps
        return -1
            
