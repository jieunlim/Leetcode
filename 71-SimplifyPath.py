#T: O(n), S: O(#dir)
class Solution:
    def simplifyPath(self, path: str) -> str:
        sol = ""
        arr = path.split("/")
        stack = []
        dellist = ["", '.', '/', '..', '//']
        for i in range(len(arr)):
            if arr[i] not in dellist:
                stack.append("/"+arr[i])
            if stack and arr[i] == '..': stack.pop()
        
        if stack == []: return "/"
        return ''.join(stack) 
