#O(n), O(1)
#42, 907, 1152, 1217
class Solution:
    def maxArea(height):
        l, r = 0, len(height)-1
        volume = 0

        while l < r:
            if height[l] < height[r]:
                volume = max((r-l)*height[l], volume)
                print(f"{l}, {r}, {height[l]}, l - volume={volume}")
                l += 1
            else:
                volume = max((r-l)*height[r], volume)
                print(f"r - volume={volume}")
                r -= 1

        return volume


    height=[1,3,5,2]
    # height =[1,8,6,2,5,4,8,3,7]
    print(maxArea(height))