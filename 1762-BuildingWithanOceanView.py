#O(n), O(1)
class Solution:
    def findBuildings(self, heights):
        maxheight = 0
        res = []
        for i in range(len(heights)-1, -1, -1):
            if heights[i]>maxheight: res.append(i)
            maxheight = max(maxheight, heights[i])
        return res[::-1]

obj = Solution()
heights = [4, 2, 3, 1]
print(obj.findBuildings(heights))