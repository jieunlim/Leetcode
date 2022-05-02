#T: O(NlogN), S: O(N)

import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        sol = []
        heap = []
        
        for i, point in enumerate(points):
            heapq.heappush(heap, (point[0]**2 + point[1]**2, i))
        
        for _ in range(k):
            sol.append(points[heapq.heappop(heap)[1]])
        
        return sol


class Solution1:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        sol = []
        dic = defaultdict(list)
        
        for x, y in points:
            dis = x**2 + y**2
            dic[dis].append([x,y])
            
        
        newdic = sorted(dic.items(), key=lambda x: x[0])
        for key, values in newdic:
            if len(sol)==k:
                return sol
            for i in values:
                if len(sol) == k:
                    return sol
                sol.append(i)
        return sol

        
        
