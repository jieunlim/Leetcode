#T: O(n)
#S: O(1)
class Solution:
    def totalMoney(self, n):
        sum = 0
        carryone = 1
        for i in range(n+1):
            if i<=7:
                sum += i
                
            elif i%7 ==0:
                sum += 7 + (i//7-1)  
                carryone = 0
            elif i > 7:
                carryone = i//7 
                sum += carryone + i%7
            
        return sum

nums = 20


obj = Solution()
print(obj.totalMoney(nums))