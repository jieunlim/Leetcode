class Solution:
    def findOcurrences(self, text: str, first: str, second: str) :
        arr = text.split(" ")
        res = []

        for i in range (len(arr)-2):
            if arr[i] == first and arr[i+1]==second:
                print(arr[i])
                res.append(arr[i+2])
        return res
                

obj = Solution()
t = "alice is a good girl she is a good student"
first = "a"
second = "good"
print(obj.findOcurrences(t, first, second))