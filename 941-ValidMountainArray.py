#T: O(n)
#S: O(1)
class Solution:
    def validMountainArray(self, arr):
        i = 0
        while i+1 < len(arr) and arr[i] < arr [i+1]:
            i +=1

        if i == 0 or i==len(arr)-1:
            return False
        
        while i+1 < len(arr) and arr[i] > arr[i+1]:
            i +=1

        return i == len(arr)-1
    
arr = [0, 1, 2, 3, 4, 3, 2, 1, 0]
obj = Solution()
print(obj.validMountainArray(arr))