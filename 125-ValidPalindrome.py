#O(n), O(1)
class Solution:
    def isPalindrome(self, s):
        i, j = 0, len(s)-1
        
        while i<j:
            if not s[i].isalpha():
                i+=1
            elif not s[j].isalphe():
                j-=1
            elif s[i].lower()!= s[j].lower():
                return False
            else:
                i+=1
                j-=1
        return True
obj = Solution()
s = "12321"
print(obj.isPalindrome(s))