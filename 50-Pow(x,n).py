class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def helper(x, n):
            if n == 0:
                return 1
            half = helper(x, n//2)
            
            print(f"half: {half}, x:{x}, n:{n}")
            if n % 2 == 0:
                return half * half
            else:
                return half * half * x
        
        
        if n<0:
            return 1/ helper(x, -n)
        else:
            return helper(x, n)
        
