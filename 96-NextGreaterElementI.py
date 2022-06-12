#O(n), O(n) , n is # of nums2
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        sol = []
        dic = {}
        stack = [nums2[0]]
        
        for i in range(1, len(nums2)):
            while stack and nums2[i] > stack[-1]:
                key = stack.pop()
                dic[key] = nums2[i]
            
            stack.append(nums2[i])
        
        for num in stack:
            dic[num] = -1
        
        for n1 in nums1:
            sol.append(dic[n1])
        
        return sol
