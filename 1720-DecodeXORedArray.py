class Solution:
      def decode(self, encoded, first):
        
        original = [first]
        for n in encoded:
            original.append(n^original[-1])
        return original


encoded = [1,2,3] 
first = 1
obj = Solution()
print(obj.decode(encoded, first))
