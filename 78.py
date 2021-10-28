class Solution(object):
   # DFS recursively
    # time O(N*2^N)
    # space O(N*2^N)
    def subsets(self, nums):

        def helper(idx, path):
            res.append(path)

            if idx >= len(nums): return

            for s in range(idx, len(nums)):
                helper(s + 1, path + [nums[s]])

        res = []
        helper(0, [])
        return res