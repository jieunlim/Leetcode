class Solution:
    def validPalindrome(self, s):
        def helper(x, y):
            while x<y:
                if s[x]!=s[y]:
                    return False
                x+=1
                y-=1
            return True

        i, j = 0, len(s)-1
        while i<j:
            if s[i]!=s[j]:
                return helper(i+1, j) or helper(i, j-1)
            i+=1
            j-=1
        return True
obj = Solution()
s = 'aba'
print(obj.validPalindrome(s))