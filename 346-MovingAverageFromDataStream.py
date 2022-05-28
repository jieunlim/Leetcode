# T: O(n) ,S: O(m), m is length of queue
class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.q = deque()
        


    def next(self, val: int) -> float:
        
        self.q.append(val)
        if len(self.q)>self.size: self.q.popleft()
        
        return sum(self.q)/len(self.q)
    
    
class MovingAverage2:

    def __init__(self, size: int):
        self.q = collections.deque(maxlen=size)

    def next(self, val: int) -> float:
        self.q.append(val)
        
        return sum(self.q) / len(self.q)