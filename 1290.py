class Solution(object):
    def getDecimalValue(self, head, res = 0):
        
        """
        :type head: ListNode
        :rtype: int
        """
        # if head == None:
        #     return res
        # else :
        #     return self.getDecimalValue(head.next, res * 2 + head.val)
        
        
        size = 0
        current = head
        res = 0
        
        while current.next:
            size += 1
            current = current.next
        
        current = head
        
        def find (current, size, res):
            
            if current:
                res += 2**size * current.val
                size -= 1
                current = current.next
                return find(current, size, res)
            
            else:
                return res
            
        
        res = find(current, size, res)
        return res  