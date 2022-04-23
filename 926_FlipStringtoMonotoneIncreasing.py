#T: O(n), S: O(1)
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        cnt_one = 0
        cnt_flip = 0
        
        for ch in s:
            if ch == '1':
                cnt_one += 1
            else:
                cnt_flip += 1
            cnt_flip = min(cnt_one, cnt_flip)
        return cnt_flip
