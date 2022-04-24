class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mystack = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        
        self.mystack.append(x);
        
    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        temp = []
        res = 0
        while self.mystack:
            temp.append(self.mystack.pop())
        res = temp.pop()
        
        
        while temp:
            self.mystack.append(temp.pop())
            
        return res
            
    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        temp = []
        res = 0
        
        while self.mystack:
            temp.append(self.mystack.pop())
        res = temp[len(temp)-1]
        
        while temp:
            self.mystack.append(temp.pop())
        return res
    
    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.mystack

