# S: O(N), T: O(N)

class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        cnt = collections.Counter(arr1 + arr2 + arr3)
        res = []
        for item, val in cnt.items():
            if val == 3:
                res.append(item)
        return res
      
      
# S: O(1), T: O(N)
class Solution2:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        res = []
        i1 = i2 = i3 = 0
        
        while i1<len(arr1) and  i2<len(arr2) and i3<len(arr3):
            if arr1[i1] == arr2[i2] == arr3[i3]:
                res.append(arr1[i1])
                i1 += 1
                i2 += 1
                i3 += 1
            else:
                if arr1[i1] < arr2[i2]:
                    i1 += 1
                elif arr2[i2] < arr3[i3]:
                    i2 += 1
                else:
                    i3 += 1
        
        
        return res
