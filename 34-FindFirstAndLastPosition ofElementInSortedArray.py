class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def find(flag):
            start, end = 0, len(nums)-1
            rtn = -1
            
            while start <= end:
                mid = start + (end-start)//2
                if nums[mid] == target:
                    rtn = mid
                    if not flag: end = mid-1
                    else: start = mid + 1
                elif nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return rtn
        
        res = [-1,-1]
        res[0], res[1] = find(0), find(1)
        return res
