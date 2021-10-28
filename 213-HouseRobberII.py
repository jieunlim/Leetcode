# 첫번째 집과 마지막 집이 연결되어 잇어서 첫번째 집을 터는경우 마지막 집을 털 수 없음
# 마지막 집을 뺀 후 최대값 계산
# 두갑의 max 를 구하면 되는 dp문제

# T: o(n)/ S: o(n)

class Solution:
    def rob(self, nums):
        def helper(idx, length):
            if idx > length: return 0
            if idx in memo: return memo[idx]
            
            memo[idx] = max(helper(idx+2, length) + nums[idx], helper(idx+1, length))

            return memo[idx]
        if len(nums) < 2: return nums[0]
        memo = {}
        r1 = helper(0, len(nums)-1)
        r2 = helper(1, len(nums))
        return max(r1, r2)

    def rob2(self, nums):
        def helper(nums):
            #preM: prepre
            #curM: pre
            preM = curM = 0
            for n in nums:
                tmp = curM
                curM = max(preM + n, curM)
                preM = tmp
            return curM
        if len(nums)<2: return nums[0]

obj = Solution()
nums = [2,3,2]
print(obj.rob(nums))
print(obj.rob2(nums))