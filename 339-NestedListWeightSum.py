#O(n)/O(n)
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        def helper(nl, depth):
            sum = 0
            for item in nl:
                if item.isInteger():
                    sum+= item.getInteger() * depth
                else:
                    sum += helper(item.getList(), depth+1)
            return sum
        return helper(nestedList, 1)
