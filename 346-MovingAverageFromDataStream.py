# T: O(n) ,S: O(m), m is size, (which is queue size)


class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.arr = deque()
        self.total = 0
    def next(self, val: int) -> float:
        self.arr.append(val)
        self.total += val
        if len(self.arr)>self.size:
            self.total -= self.arr.popleft()
        return self.total/len(self.arr)


# T: O(n) ,S: O(m), m is length of queue
class MovingAverage2:

    def __init__(self, size: int):
        self.size = size
        self.q = deque()
        


    def next(self, val: int) -> float:
        
        self.q.append(val)
        if len(self.q)>self.size: self.q.popleft()
        
        return sum(self.q)/len(self.q)
    
    
class MovingAverage3:

    def __init__(self, size: int):
        self.q = collections.deque(maxlen=size)

    def next(self, val: int) -> float:
        self.q.append(val)
        
        return sum(self.q) / len(self.q)
