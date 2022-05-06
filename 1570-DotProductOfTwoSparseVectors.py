#  O(n) / O(n)
class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        sol = 0
        for i, j in zip(self.nums, vec.nums):
            sol += i*j
        return sol

# O(n) / O(non-zero elements)
class SparseVector2:
    def __init__(self, nums: List[int]):
        self.dict = {}
        for i in range(len(nums)):
            if nums[i]: self.dict[i] = nums[i]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        sol = 0
        for i, n in self.dict.items():
            print(i, n)
            if i in vec.dict:
                sol += n*vec.dict[i]
        return sol
