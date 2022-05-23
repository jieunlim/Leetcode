class Solution1:
    def nextPermutation(self, nums: List[int]) -> None:
              
        i = j = len(nums)-1
        
        #find peak
        
        while i>0 and nums[i-1] >= nums[i]:
            i-=1
        if i == 0:
            return nums.reverse()
        
        #find a next bigger value, then swap
        
        k = i-1
        
        while j>=0 and nums[k]>=nums[j]:
            j-=1
        nums[k], nums[j] = nums[j], nums[k]
        
        #reverse remaining
        
        l, r = k+1, len(nums)-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l+=1
            r-=1

            
  
class Solution2:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = j = len(nums)-1
        
        #find peak
        
        while i>0 and nums[i-1] >= nums[i]:
            i-=1
        if i == 0:
            return nums.reverse()
        
        #find a bigger value, then swap
        print(i)
        
        k = i-1
        
        while j>=0 and nums[k]>=nums[j]:
            j-=1
        nums[k], nums[j] = nums[j], nums[k]
        
        #reverse remaining
        
        nums[k+1:] = sorted(nums[k+1:])
            
