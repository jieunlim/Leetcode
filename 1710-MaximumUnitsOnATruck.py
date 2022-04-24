#T:O(nlogn) S: O(1)
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse= True)
        sol = 0
        
        for i in range(len(boxTypes)):
            if truckSize > 0:
                sol += min(boxTypes[i][0], truckSize) * boxTypes[i][1]
            truckSize -= boxTypes[i][0]
        return sol
