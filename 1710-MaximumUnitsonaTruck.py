#T: O(n*logn), S: O(1)
class Solution:
    def maximumUnits(self, boxTypes, truckSize):
        boxTypes.sort(key = lambda x: x[1], reverse=True)
        ans = 0
        for i in range(0, len(boxTypes)):
            unit = min(boxTypes[i][0], truckSize)
            ans += unit * boxTypes[i][1]
            truckSize -= unit
            if truckSize==0:
                break
        return ans

obj = Solution()
boxTypes = [[1,3],[2,2],[3,1]]
truckSize = 4
print(obj.maximumUnits(boxTypes, truckSize))
