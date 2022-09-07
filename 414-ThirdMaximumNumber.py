class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = second = third = float(-inf)
        for num in nums:
            if num > first:
                first, second, third = num, first, second
            elif num == first: continue
            elif num > second:
                second, third = num, second
            elif num == second: continue
            elif num > third:
                third = num
        return third if third != float(-inf) else first
