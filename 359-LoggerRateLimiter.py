#T: O(1), S:O(N) where N is # of unique message
class Logger:

    def __init__(self):
        self.dic = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        
        if message in self.dic:
            if self.dic[message] <= timestamp:
                self.dic[message] = timestamp + 10
                return True
            else:
                return False
        else: 
            self.dic[message] = timestamp + 10
            return True
