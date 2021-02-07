class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m -1
        p2 = n -1
        p3 = m + n - 1
        
        while p1>=0 and p2>=0:
            if nums1[p1] < nums2[p2]:
                nums1[p3] = nums2[p2]
                p2 -=1
            else: 
                nums1[p3] = nums1[p1]
                p1 -=1
            p3 -=1
        print(f"p1={p1}, nums1={nums1}, {nums1[:p2+1]}, {nums2[:p2+1]}")
            
        nums1[:p2+1] = nums2[:p2+1]


nums1=[2,0]
m=1
nums2=[1]
n=1
obj = Solution()
obj.merge(nums1, m, nums2, n)
print(nums1)
# time O(m+n), space O(1)