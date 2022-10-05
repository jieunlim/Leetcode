#Time: O(n), Space: O(1)
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        seen = set()
        dic = {c : i for i, c in enumerate(s)}
        
        for i, c in enumerate(s):
            if c not in seen:
                while stack and c < stack[-1] and dic[stack[-1]] > i:
                    seen.remove(stack.pop())
                seen.add(c)
                stack.append(c)
        return ''.join(stack)
