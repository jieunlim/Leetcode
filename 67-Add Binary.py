class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x, y = int(a, 2), int(b, 2) 
        print(x, y) #binary to 10
       
        while y:
            #x, y = x ^ y, (x & y) << 1
            ans = x ^ y
            carry = (x & y) << 1
            x = ans
            y = carry
            print(bin(x), bin(y))
            print(x, y)
        return bin(x)[2:]
