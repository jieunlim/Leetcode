#O(n), O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l<r:
            print(s[l], s[r])
            if not s[l].isalpha() and not s[l].isdigit():
                l+=1
                continue
            if not s[r].isalpha() and not s[r].isdigit():
                r-=1
                continue
            if s[l].lower() == s[r].lower():
                l+=1
                r-=1
            else:
                return False
        return True
    
class Solution2:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l<r:
            
            if not s[l].isalnum():
                l+=1
                continue
            if not s[r].isalnum():
                r-=1
                continue
            if s[l].lower() == s[r].lower():
                l+=1
                r-=1
            else:
                return False
        return True
            
            
obj = Solution()
s = "12321"
print(obj.isPalindrome(s))
