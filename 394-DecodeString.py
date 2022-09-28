class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        res = []
        
        curNum, curStr = "", ""
        
        for c in s:
            if c=='[':
                stack.append(curStr)
                stack.append(int(curNum))
                curStr, curNum = "", ""
            elif c == ']':
                num = stack.pop()
                string = stack.pop()
                curStr = string + (num * curStr)
            elif c.isdigit():
                curNum += c
            elif c.isalpha():
                curStr += c
        return curStr
