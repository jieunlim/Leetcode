#T: O(NlogN), S:O(N)
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        room = 0
        dic = defaultdict(int)
        res = 0
        
        for start, end in intervals:
            dic[start] += 1
            dic[end] -= 1
        
        sorted_dict = dict(sorted(dic.items()))
        
        for time in sorted_dict:
            room += sorted_dict[time]
            res = max(res, room)
            
        return res
    


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
      
