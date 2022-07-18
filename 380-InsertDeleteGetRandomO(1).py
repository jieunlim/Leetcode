class RandomizedSet1: # GetRandom: O(n)

    def __init__(self):
        self.s = set()

    def insert(self, val: int) -> bool:
        if val not in self.s: 
            self.s.add(val)
            return True
        else: return False        

    def remove(self, val: int) -> bool:
        if val in self.s:
            self.s.remove(val)
            return True
        else: return False

    def getRandom(self) -> int:
        # O(n)/O(n)
        ranlist = list(self.s)
        idx = random.randint(0, len(self.s)-1)
        return ranlist[idx]
        
        
### GetRandom: O(1) 
class RandomizedSet2:

    def __init__(self):
        self.dic = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        
        if val not in self.dic:
            self.arr.append(val) #[1,2,3] 
            self.dic[val] = len(self.arr)-1 #{1:0, 2:1, 3:2} value: array index
            return True
        else: return False        

    def remove(self, val: int) -> bool:
        
        if val in self.dic:  # id delete 2: arr = [1,2,3], dic = {1:0, 2:1, 3:2}
            #change last element location to index we want to replace
            self.dic[self.arr[-1]] = self.dic[val] # dic[3] = 1 : {1:0, 2:1, 3:1}
            self.arr[self.dic[val]] = self.arr[-1] # arr[1] = 3 : [1,3,3]
            self.dic.pop(val) # {1:0, 3:1}
            self.arr.pop() # [1,2]
            
            return True
        else: return False

    def getRandom(self) -> int:
        return random.choice(self.arr)
