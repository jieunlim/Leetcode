class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for i in range (len(nums1)):
            for j in range (len(nums2)):
                if nums1[i]==nums2[j]:
                    result.append(nums1[i])
                    nums1[i] = 'a'
                    nums2[j] = 'b'
                
        return result
        #very slow, O(n*m)
