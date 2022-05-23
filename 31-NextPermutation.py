#T: O(N), S: O(1)
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
        
        n = len(nums)-1
        peak = -1
        second_peak = -1
        
        # find a peak
        
        for i in range(n-1, -1, -1):
            
            if nums[i]<nums[i+1]: 
                peak = i
                break
 
        if peak == -1: 
            nums.reverse() 
            return

        # find next bigger value
        
        for j in range(n, peak, -1):
            
            if nums[j] > nums[peak]:
                second_peak = j
                break
                
        nums[peak], nums[second_peak] = nums[second_peak], nums[peak]
        
        # reverse remaining 
        print(nums)
        nums[peak+1:] = sorted(nums[peak+1:])
