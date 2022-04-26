#T: O(NlogN), S:O(N)
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        maxroom = 0
        sol = 0
        n = len(intervals)
        m = defaultdict(int)
        
        if len(intervals) == 1 : return 1
        
        for i in range(n):
            start = intervals[i][0]
            end = intervals[i][1]
            m[start]+= 1
            m[end]-= 1
        
        sorted_m = dict(sorted(m.items()))
        for r in sorted_m:
            sol += sorted_m[r]
            maxroom = max(maxroom, sol)
                
        return maxroomclass Solution:

# time O(nlgn), space O(n)      
class Solution2:
  
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        if not intervals: return 0
        
        room = []
        intervals.sort(key = lambda x:x[0])
        
        heapq.heappush(room, intervals[0][1])
        
        for i in intervals[1:]:
            if room[0] <= i[0]:
                heapq.heappop(room)
                
            heapq.heappush(room, i[1])
        return len(room)
 
# Same but simple and clean

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        room = []
        intervals.sort(key = lambda x: x[0])
        
        for start, end in intervals:
           
            if room and room[0] <= start:
                heapq.heappop(room) # O(logn)
            
            heapq.heappush(room, end)  # O(logn)
        return len(room)
      
