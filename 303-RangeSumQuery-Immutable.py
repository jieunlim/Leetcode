# O(n) for init, O(1) for query / O(n)

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        for i in range(1, len(nums)):
            self.nums[i] = nums[i-1] + nums[i] 

    def sumRange(self, left: int, right: int) -> int:
        return self.nums[right] if left == 0 else self.nums[right] - self.nums[left-1]
