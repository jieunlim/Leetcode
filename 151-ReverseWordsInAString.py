# Solution 1 - Built-in function (split, reversed)
# O(n) / O(n)
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))


# O(n) / O(n)
class Solution2:
    def reverseWords(self, s: str) -> str:
        res = []
        stack = []
        list_s = s.split(" ")
        for word in list_s:
            stack.append(word)
        print(stack)
        
        while stack:
            word = stack.pop()
            if word != "":
                res.append(word)
        
        
        return " ".join(res)
