#T: O(n), S: O(1)
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        '''
        1. create dic - val, loc
        2. update to recent loc if available
        3. length : i - low + 1
        4. res = max(res, length)
        5. if len dic > k: find min low and find val in str then delete in dic, and then increase low += 1
        '''
        res = low = 0
        dic = {}
        
        for i, ch in enumerate(s):
            dic[ch] = i
            if len(dic) > k:
                low = min(dic.values())
                del dic[s[low]]
                low += 1
            
            length = i - low + 1
            res = max(res, length)
        return res
